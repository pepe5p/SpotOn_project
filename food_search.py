from translation import translate_ingr
from database import Database
import requests
import json


db = Database()


# TODO: tests
def find_food(included_ingr: list, excluded_ingr: list | None = None) -> None:
    """
    Function that finds list of meals and suggest what to eat.

    Store output in HTML file.

    :param included_ingr: list of ingredients to include
    :param excluded_ingr: list of ingredients to exclude
    """

    if excluded_ingr is None:
        excluded_ingr = ["plums"]

    included_ingr.sort()
    excluded_ingr.sort()

    data = db.fetch_output(incl_ingr=included_ingr, excl_ingr=excluded_ingr)
    if not data:
        data = get_data_from_api(included_ingr, excluded_ingr)
    data = json.loads(data)

    if len(data) == 0:
        print("\nSorry, we don't have meals with that ingredients.")
        return

    create_html_file(data)


def get_data_from_api(included_ingr: list, excluded_ingr: list) -> str:
    """
    Function that gets JSON response from API of https://api.spoonacular.com.

    Transforms data to smaller and more comfortable format.

    Store data to DB and returns that data.

    :param included_ingr: list of ingredients to include
    :param excluded_ingr: list of ingredients to exclude
    :return: data from API
    """

    with open("spoonacular_api_key.txt", "r") as file:
        api_key = file.read()

    query = ("https://api.spoonacular.com/recipes/complexSearch?"
             f"apiKey={api_key}"
             f"&includeIngredients={','.join([ingr for ingr in included_ingr])}"
             f"&excludeIngredients={','.join([ingr for ingr in excluded_ingr])}"
             "&fillIngredients=true"
             "&addRecipeNutrition=true"
             "&number=5"
             "&sort=min-missing-ingredients")
    # print("\n query: ", query, '\n\n')
    data_json = requests.get(query).text
    data = json.loads(data_json)

    new_data = []
    for recipe in data["results"]:
        nutrition = recipe["nutrition"]["nutrients"]
        recipe_dict = {
            "name": recipe['title'],
            "img_url": recipe['image'],
            "used_ingr": [ingr["name"] for ingr in recipe["usedIngredients"]],
            "missed_ingr": [ingr["name"] for ingr in recipe["missedIngredients"]],
            "carbs": (nutrition[3]['amount'], nutrition[3]["unit"]),
            "proteins": (nutrition[8]['amount'], nutrition[8]["unit"]),
            "calories": (nutrition[0]['amount'], nutrition[0]["unit"])
        }
        new_data.append(recipe_dict)

    # TODO: ask for relation between (min carbs, max proteins)
    new_data.sort(key=lambda result: 3*result["carbs"][0] - result["proteins"][0])

    new_data_json = json.dumps(new_data)
    db.insert(None, str(included_ingr), str(excluded_ingr), new_data_json)

    return new_data_json


def create_html_file(data: list) -> None:
    """
    :param data: list of recipes to display
    """

    best = data[0]
    text = f'We suggest you to choose {best["name"]}, ' \
           f'because it has only {best["carbs"][0]}{best["carbs"][1]} carbs, ' \
           f'and {best["proteins"][0]}{best["proteins"][1]} proteins.<br><br><br><br>'
    for recipe in data:
        text += generate_recipe_text(recipe)

    extended_ingr = best['used_ingr'] + best['missed_ingr']
    normalized_ingr = [ingr.lower().replace(" ", "-") + str(int(i) + 1)
                       for i, ingr in enumerate(extended_ingr)]

    file_name = "_".join(normalized_ingr)
    file_name = "outputs/" + file_name + ".html"

    print("\noutput stored in file:", file_name)

    with open(file_name, "w") as file:
        file.write(text)


def generate_recipe_text(recipe: dict) -> str:
    """
    :param recipe: data of recipe in dictionary
    :return:
    """
    used_ingr = ''.join(map(lambda ingr: f'<br>* {ingr}', recipe['used_ingr']))
    missed_ingr = ''.join(map(lambda ingr: f'<br>* {ingr} - {translate_ingr(ingr)}', recipe['missed_ingr']))

    return (f"{recipe['name']}"
            f"<br><img src='{recipe['img_url']}'>"
            f"<br>used ingredients: {used_ingr}"
            f"<br>missed ingredients: {missed_ingr}"
            f"<br>carbs: {recipe['carbs'][0]}{recipe['carbs'][1]}"
            f"<br>proteins: {recipe['proteins'][0]}{recipe['proteins'][1]}"
            f"<br>calories: {recipe['calories'][0]}{recipe['calories'][1]}"
            "<br><br><br><br>")
