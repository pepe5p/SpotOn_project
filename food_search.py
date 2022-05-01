from translation import translate_ingr
from database import Database
import requests
import json
import string


db = Database()


def get_data_from_api(included_ingr: list, excluded_ingr: list) -> string:
    """function that gets JSON response from API of https://api.spoonacular.com"""

    '''getting key to spoonacular API'''
    with open("spoonacular_api_key.txt", "r") as f:
        api_key = f.read()

    '''getting data from API'''
    # TODO: better query
    query = ("https://api.spoonacular.com/recipes/complexSearch?"
             f"apiKey={api_key}"
             f"&includeIngredients={','.join([ingr for ingr in included_ingr])}"
             f"&excludeIngredients={','.join([ingr for ingr in excluded_ingr])}"
             "&fillIngredients=true"
             "&addRecipeNutrition=true"
             "&number=5"
             "&sort=min-missing-ingredients")
    print("\nquery: ", query, '\n\n')
    raw_data = requests.get(query).text

    '''add record to DB'''
    # TODO: maybe not store whole JSON response?
    db.insert(None, str(included_ingr), str(excluded_ingr), raw_data)

    return raw_data


def find_food(included_ingr: list, excluded_ingr: list = None) -> None:
    """function that finds list of meals and suggest what to eat and store output in HTML file"""

    if excluded_ingr is None:
        excluded_ingr = ["plums"]

    '''sorting lists to make them well-defined
    important while checking input existence in DB'''
    included_ingr.sort()
    excluded_ingr.sort()

    '''checking if input is in DB'''
    data = db.fetch_output(incl_ingr=included_ingr, excl_ingr=excluded_ingr)
    if not data:
        data = get_data_from_api(included_ingr, excluded_ingr)

    '''parsing data from JSON and sorting by carbs ASC, then proteins DESC'''
    data = json.loads(data)
    # TODO: ask for relationship between (min carbs, max proteins)
    data["results"].sort(key=lambda result: (result["nutrition"]["nutrients"][3]["amount"],
                                             -result["nutrition"]["nutrients"][8]["amount"]))

    if data["totalResults"] == 0:
        print("\nsorry, we don't have meals like that")
        return

    best = data["results"][0]
    text = f'We suggest you to choose {best["title"]}<br><br><br><br>'

    '''loading all data to string'''
    for recipe in data["results"]:
        nutrition = recipe["nutrition"]["nutrients"]
        used_ingr = [ingr["name"] for ingr in recipe["usedIngredients"]]
        missed_ingr = [ingr["name"] for ingr in recipe["missedIngredients"]]

        recipe_data = (f"name: {recipe['title']}"
                       f"<br><img src='{recipe['image']}'>"
                       f"<br>used ingredients: {[ingr for ingr in used_ingr]}"
                       f"<br>missed ingredients: {[f'{ingr}-{translate_ingr(ingr)}' for ingr in missed_ingr]}"
                       f"<br>carbs: {nutrition[3]['amount']}"
                       f"<br>proteins: {nutrition[8]['amount']}"
                       f"<br>calories: {nutrition[0]['amount']}"
                       "<br><br><br><br>")
        text += recipe_data

    '''creating HTML output file'''
    normalized_ingr = [ingr["name"].lower().replace(" ", "-") + str(int(i) + 1)
                       for i, ingr in enumerate(best["extendedIngredients"])]

    file_name = "_".join(normalized_ingr)
    file_name = "outputs/" + file_name + ".html"

    print("\noutput stored in file:", file_name)

    with open(file_name, "w") as f:
        f.write(text)
