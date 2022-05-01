from translation import translate_ingr
from database import Database
import requests
import json


db = Database()


class Recipe:   # TODO: delete class
    def __init__(self, name, picture, used_ingr, missed_ingr, carbs, proteins, cals):
        self.name = name
        self.picture = picture
        self.used_ingr = used_ingr
        self.missed_ingr = missed_ingr
        self.extended_ingr = used_ingr + missed_ingr
        self.carbs = carbs
        self.proteins = proteins
        self.cals = cals

    def to_html(self):
        return (f"name: {self.name}"
                f"<br><img src='{self.picture}'>"
                f"<br>used ingredients: {str(self.used_ingr)}"
                f"<br>missed ingredients: {[(ingr, translate_ingr(ingr)) for ingr in self.missed_ingr]}"
                f"<br>carbs: {self.carbs }"
                f"<br>proteins: {self.proteins}"
                f"<br>calories: {self.cals}"
                "<br><br><br><br>")


def get_data_from_api(included_ingr: list, excluded_ingr: list):

    """getting key to spoonacular API"""
    with open("spoonacular_api_key.txt", "r") as f:
        api_key = f.read()

    '''getting data from API'''
    query = ("https://api.spoonacular.com/recipes/complexSearch?"
             f"apiKey={api_key}"
             f"&includeIngredients={','.join([ingr for ingr in included_ingr])}"
             f"&excludeIngredients={','.join([ingr for ingr in excluded_ingr])}"
             "&fillIngredients=true"
             "&addRecipeNutrition=true"
             "&number=5"
             "&sort=min-missing-ingredients")
    print("query: ", query, '\n\n')
    raw_data = requests.get(query).text

    '''add record to DB'''
    db.insert(None, str(included_ingr), str(excluded_ingr), raw_data)

    # print(raw_data)
    return raw_data


def find_food(included_ingr: list, excluded_ingr: list = None) -> None:

    if excluded_ingr is None:
        excluded_ingr = ["plums"]

    included_ingr.sort()
    excluded_ingr.sort()

    '''checking if input is in DB'''
    data = db.fetch_output(incl_ingr=included_ingr, excl_ingr=excluded_ingr)
    if data:
        data = data[0][0]
    else:
        print("Using API")
        data = get_data_from_api(included_ingr, excluded_ingr)

    data = json.loads(data)
    # print(data['results'])
    data["results"].sort(key=lambda result: (result["nutrition"]["nutrients"][3]["amount"],
                                             -1 * result["nutrition"]["nutrients"][8]["amount"]))
    # TODO: ask for relationship between (min carbs, max proteins)

    best = data["results"][0]
    text = f'We suggest you to choose {best["title"]}<br><br><br><br>'

    '''loading all data'''
    for recipe in data["results"]:
        nutrition = recipe["nutrition"]["nutrients"]

        recipe_data = Recipe(recipe["title"],
                             recipe["image"],
                             [ingr["name"] for ingr in recipe["usedIngredients"]],
                             [ingr["name"] for ingr in recipe["missedIngredients"]],
                             nutrition[3]["amount"],
                             nutrition[8]["amount"],
                             nutrition[0]["amount"])
        text += recipe_data.to_html()

    '''creating HTML output file'''
    normalized_ingr = [ingr["name"].lower().replace(" ", "-") + str(int(i) + 1)
                       for i, ingr in enumerate(best["extendedIngredients"])]

    file_name = "_".join(normalized_ingr)
    file_name += ".html"

    with open(file_name, "w") as f:
        f.write(text)
