from src.food_search import generate_query, get_data_from_api, create_html_file, generate_recipe_text
from unittest.mock import patch
from unittest import TestCase
from test_data import data1, data2, result1, result2    # to test_get_data_from_api


class FoodSearchTest(TestCase):

    def test_generate_query(self) -> None:

        with open("spoonacular_api_key.txt", "r") as file:
            api_key = file.read()

        provided_incl_ingr_list = [
            ['cheese', 'ham'],
            ['cheese', 'ham'],
            []
        ]
        provided_excl_ingr_list = [
            ['plums'],
            ['bread'],
            []
        ]
        expected_results = []
        for i in range(1, 4):
            with open(f"tests_data/generate_query/result{i}.txt", "r") as file:
                text = file.read()
                text = text.replace("API_KEY", api_key)
                expected_results.append(text)

        for provided_incl_ingr, provided_excl_ingr, expected_result in \
                zip(provided_incl_ingr_list, provided_excl_ingr_list, expected_results):
            actual_result = generate_query(provided_incl_ingr, provided_excl_ingr)
            self.assertEqual(actual_result, expected_result)

    @patch("requests.get")
    def test_get_data_from_api(self, mock_get) -> None:

        provided_api_response_list = [data1, data2]
        expected_results = [result1, result2]

        for provided_api_response, expected_result in zip(provided_api_response_list, expected_results):
            mock_get.return_value = provided_api_response
            actual_result = get_data_from_api("")
            self.assertEqual(actual_result, expected_result)

    def test_create_html_file(self) -> None:

        provided_incl_ingr_list = [
            ['tomato'],
            []
        ]
        provided_data_list = [
            [
                {
                    "name": "Simple Spinach and Tomato Frittata",
                    "img_url": "https://spoonacular.com/recipeImages/769775-312x231.jpg",
                    "used_ingr": ["cherry tomatoes"],
                    "missed_ingr": ["burger skillet", "eggs", "spinach leaves"],
                    "carbs": (7.32, "g"),
                    "proteins": (12.62, "g"),
                    "calories": (156.15, "kcal")
                }
            ],
            [
                {
                    "name": "",
                    "img_url": "",
                    "used_ingr": [],
                    "missed_ingr": [],
                    "carbs": (None, None),
                    "proteins": (None, None),
                    "calories": (None, None)
                }
            ],
        ]
        expected_names = [
            "tomato1.html",
            "none1.html"
        ]
        expected_results = [
            "We suggest you to choose Simple Spinach and Tomato Frittata, because it has only 7.32g carbs, and 12.62g "
            "proteins.<br><br><br><br>Simple Spinach and Tomato Frittata<br><img "
            "src='https://spoonacular.com/recipeImages/769775-312x231.jpg'><br>used ingredients: <br>* cherry "
            "tomatoes<br>missed ingredients: <br>* burger skillet - patelnia do burgerów<br>* eggs - jajka<br>* "
            "spinach leaves - liście szpinaku<br>carbs: 7.32g<br>proteins: 12.62g<br>calories: "
            "156.15kcal<br><br><br><br>",
            "We suggest you to choose , because it has only NoneNone carbs, and NoneNone "
            "proteins.<br><br><br><br><br><img src=''><br>used ingredients: <br>missed ingredients: <br>carbs: "
            "NoneNone<br>proteins: NoneNone<br>calories: NoneNone<br><br><br><br>"
        ]

        for provided_incl_ingr, provided_data, expected_name, expected_result in \
                zip(provided_incl_ingr_list, provided_data_list, expected_names, expected_results):

            file_name = create_html_file(provided_incl_ingr, provided_data)
            self.assertEqual(file_name, f"html_outputs/{expected_name}")

            with open(file_name, "r") as file:
                actual_result = file.read()

            self.assertEqual(actual_result, expected_result)

    @patch("src.food_search.translate_ingr")
    def test_generate_recipe_text(self, mock_translate) -> None:

        mock_translate.return_value = ""

        provided_recipes = [
            {
                "name": "Simple Spinach and Tomato Frittata",
                "img_url": 'https://spoonacular.com/recipeImages/769775-312x231.jpg',
                "used_ingr": ["cherry tomatoes"],
                "missed_ingr": ["burger skillet", "eggs", "spinach leaves"],
                "carbs": (7.32, "g"),
                "proteins": (12.62, "g"),
                "calories": (156.15, "kcal")
            },
            {
                "name": "",
                "img_url": "",
                "used_ingr": [],
                "missed_ingr": [],
                "carbs": (None, None),
                "proteins": (None, None),
                "calories": (None, None)
            },
            {
                "name": "Jalapeno Queso With Goat Cheese",
                "img_url": "https://spoonacular.com/recipeImages/648368-312x231.jpg",
                "used_ingr": ["canned tomatoes"],
                "missed_ingr": ["goat cheese", "jalapeno pepper", "hot sauce"],
                "carbs": (17.58, "g"),
                "proteins": (31.71, "g"),
                "calories": (474.18, "kcal")
            }
        ]
        expected_results = []
        for i in range(1, 4):
            with open(f"tests_data/generate_recipe_text/result{i}.txt", "r") as file:
                expected_results.append(file.read())

        for provided_recipe, expected_result in zip(provided_recipes, expected_results):
            actual_result = generate_recipe_text(provided_recipe)
            self.assertEqual(actual_result, expected_result)
