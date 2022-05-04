from .translation import translate_ingr
from .database import Database
import requests
import json


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

    db = Database()
    data = db.fetch_output(incl_ingr=included_ingr, excl_ingr=excluded_ingr)
    if not data:
        query = generate_query(included_ingr, excluded_ingr)
        data = get_data_from_api(query)
        db.insert(None, str(included_ingr), str(excluded_ingr), data)

    data = json.loads(data)

    if len(data) == 0:
        print("\nSorry, we don't have meals with these ingredients.")
        return

    file_name = create_html_file(included_ingr, data)

    print("\nOutput stored in file:", file_name)


def generate_query(included_ingr: list, excluded_ingr: list) -> str:
    """
    :return: query prepared to be sent
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

    return query


def get_data_from_api(query: str) -> str:
    """
    Function that gets JSON response from API of https://api.spoonacular.com.

    Transforms data to smaller and more comfortable format.

    :return: data from API
    """

    data_json = requests.get(query).text
    data = json.loads(data_json, strict=False)

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

    new_data.sort(key=lambda result: 3*result["carbs"][0] - result["proteins"][0])
    new_data_json = json.dumps(new_data)

    return new_data_json


def create_html_file(included_ingr: list, recipes: list) -> str:
    """
    :param included_ingr: necessary to name file correctly
    :param recipes: list of recipes to display
    """
    if not included_ingr:
        included_ingr = ['none']

    best_recipe = recipes[0]
    text = f'We suggest you to choose {best_recipe["name"]}, ' \
           f'because it has only {best_recipe["carbs"][0]}{best_recipe["carbs"][1]} carbs, ' \
           f'and {best_recipe["proteins"][0]}{best_recipe["proteins"][1]} proteins.<br><br><br><br>'
    for recipe in recipes:
        text += generate_recipe_text(recipe)

    normalized_ingr = [ingr.lower().replace(" ", "-") + str(int(i) + 1)
                       for i, ingr in enumerate(included_ingr)]

    file_name = "_".join(normalized_ingr)
    file_name = "html_outputs/" + file_name + ".html"

    with open(file_name, "w") as file:
        file.write(text)

    return file_name


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
