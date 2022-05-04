from src.food_search import generate_query, get_data_from_api, create_html_file, generate_recipe_text
from unittest.mock import patch
from unittest import TestCase


class StringWithAttributeText:
    def __init__(self, text: str) -> None:
        self.text = text


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

        provided_api_response_list = [
            StringWithAttributeText(r'''{"results":[{"vegetarian":true,"vegan":true,"glutenFree":true,
            "dairyFree":true,"veryHealthy":false,"cheap":false,"veryPopular":false,"sustainable":false,
            "weightWatcherSmartPoints":4,"gaps":"no","lowFodmap":true,"aggregateLikes":1,"spoonacularScore":79.0,
            "healthScore":27.0,"creditsText":"Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
            "license":"CC BY 3.0","sourceName":"Foodista","pricePerServing":90.14,"extendedIngredients":[{"id":11527,
            "aisle":"Produce","image":"green-tomato.png","consistency":"solid","name":"green tomato",
            "nameClean":"green tomato","original":"1 large green tomato","originalName":"green tomato","amount":1.0,
            "unit":"large","meta":["green"],"measures":{"us":{"amount":1.0,"unitShort":"large","unitLong":"large"},
            "metric":{"amount":1.0,"unitShort":"large","unitLong":"large"}}},{"id":4053,"aisle":"Oil, Vinegar, 
            Salad Dressing","image":"olive-oil.jpg","consistency":"liquid","name":"olive oil","nameClean":"olive 
            oil","original":"1 tablespoon of olive oil","originalName":"olive oil","amount":1.0,"unit":"tablespoon",
            "meta":[],"measures":{"us":{"amount":1.0,"unitShort":"Tbsp","unitLong":"Tbsp"},"metric":{"amount":1.0,
            "unitShort":"Tbsp","unitLong":"Tbsp"}}},{"id":10211111,"aisle":"Ethnic Foods;Spices and Seasonings",
            "image":"dried-sumac.jpg","consistency":"solid","name":"sumac","nameClean":"sumac","original":"1 teaspoon 
            of sumac powder","originalName":"sumac powder","amount":1.0,"unit":"teaspoon","meta":[],"measures":{
            "us":{"amount":1.0,"unitShort":"tsp","unitLong":"teaspoon"},"metric":{"amount":1.0,"unitShort":"tsp",
            "unitLong":"teaspoon"}}},{"id":2064,"aisle":"Produce;Spices and Seasonings","image":"mint.jpg",
            "consistency":"solid","name":"mint leaves","nameClean":"mint","original":"A handful of sage and mint 
            leaves, finely chopped","originalName":"A of sage and mint leaves, finely chopped","amount":1.0,
            "unit":"handful","meta":["finely chopped"],"measures":{"us":{"amount":1.0,"unitShort":"handful",
            "unitLong":"handful"},"metric":{"amount":1.0,"unitShort":"handful","unitLong":"handful"}}}],"id":645555,
            "title":"Green Tomato Salad","readyInMinutes":45,"servings":1,
            "sourceUrl":"https://www.foodista.com/recipe/KWMJ8SPX/green-tomato-salad",
            "image":"https://spoonacular.com/recipeImages/645555-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":168.42,"unit":"kcal","percentOfDailyNeeds":8.42},{"name":"Fat",
            "amount":14.4,"unit":"g","percentOfDailyNeeds":22.16},{"name":"Saturated Fat","amount":1.99,"unit":"g",
            "percentOfDailyNeeds":12.46},{"name":"Carbohydrates","amount":9.88,"unit":"g",
            "percentOfDailyNeeds":3.29},{"name":"Net Carbohydrates","amount":7.56,"unit":"g",
            "percentOfDailyNeeds":2.75},{"name":"Sugar","amount":7.28,"unit":"g","percentOfDailyNeeds":8.09},
            {"name":"Cholesterol","amount":0.0,"unit":"mg","percentOfDailyNeeds":0.0},{"name":"Sodium",
            "amount":25.18,"unit":"mg","percentOfDailyNeeds":1.09},{"name":"Protein","amount":2.33,"unit":"g",
            "percentOfDailyNeeds":4.67},{"name":"Vitamin C","amount":43.86,"unit":"mg","percentOfDailyNeeds":53.16},
            {"name":"Vitamin A","amount":1338.36,"unit":"IU","percentOfDailyNeeds":26.77},{"name":"Vitamin K",
            "amount":26.81,"unit":"µg","percentOfDailyNeeds":25.53},{"name":"Vitamin E","amount":2.71,"unit":"mg",
            "percentOfDailyNeeds":18.05},{"name":"Manganese","amount":0.23,"unit":"mg","percentOfDailyNeeds":11.45},
            {"name":"Potassium","amount":394.18,"unit":"mg","percentOfDailyNeeds":11.26},{"name":"Fiber",
            "amount":2.32,"unit":"g","percentOfDailyNeeds":9.29},{"name":"Vitamin B5","amount":0.92,"unit":"mg",
            "percentOfDailyNeeds":9.24},{"name":"Copper","amount":0.18,"unit":"mg","percentOfDailyNeeds":8.85},
            {"name":"Vitamin B6","amount":0.15,"unit":"mg","percentOfDailyNeeds":7.63},{"name":"Vitamin B1",
            "amount":0.11,"unit":"mg","percentOfDailyNeeds":7.5},{"name":"Iron","amount":1.21,"unit":"mg",
            "percentOfDailyNeeds":6.72},{"name":"Phosphorus","amount":53.88,"unit":"mg","percentOfDailyNeeds":5.39},
            {"name":"Magnesium","amount":21.4,"unit":"mg","percentOfDailyNeeds":5.35},{"name":"Folate",
            "amount":20.94,"unit":"µg","percentOfDailyNeeds":5.24},{"name":"Vitamin B2","amount":0.08,"unit":"mg",
            "percentOfDailyNeeds":4.91},{"name":"Vitamin B3","amount":0.98,"unit":"mg","percentOfDailyNeeds":4.89},
            {"name":"Calcium","amount":33.52,"unit":"mg","percentOfDailyNeeds":3.35},{"name":"Zinc","amount":0.17,
            "unit":"mg","percentOfDailyNeeds":1.15},{"name":"Selenium","amount":0.73,"unit":"µg",
            "percentOfDailyNeeds":1.04}],"properties":[{"name":"Glycemic Index","amount":0.0,"unit":""},
            {"name":"Glycemic Load","amount":0.0,"unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,
            "unit":""},{"name":"Petunidin","amount":0.0,"unit":""},{"name":"Delphinidin","amount":0.0,"unit":""},
            {"name":"Malvidin","amount":0.0,"unit":""},{"name":"Pelargonidin","amount":0.0,"unit":""},
            {"name":"Peonidin","amount":0.0,"unit":""},{"name":"Catechin","amount":0.0,"unit":""},
            {"name":"Epigallocatechin","amount":0.0,"unit":""},{"name":"Epicatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},{"name":"Epigallocatechin 3-gallate",
            "amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins","amount":0.0,
            "unit":""},{"name":"Eriodictyol","amount":1.24,"unit":"mg"},{"name":"Hesperetin","amount":0.41,
            "unit":"mg"},{"name":"Naringenin","amount":0.0,"unit":""},{"name":"Apigenin","amount":0.23,"unit":"mg"},
            {"name":"Luteolin","amount":0.52,"unit":"mg"},{"name":"Isorhamnetin","amount":0.0,"unit":"mg"},
            {"name":"Kaempferol","amount":0.0,"unit":"mg"},{"name":"Myricetin","amount":0.0,"unit":""},
            {"name":"Quercetin","amount":0.0,"unit":"mg"},{"name":"Theaflavin-3,3'-digallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate",
            "amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,"unit":""}],"ingredients":[{"id":11527,
            "name":"green tomato","amount":1.0,"unit":"large","nutrients":[{"name":"Vitamin B3","amount":0.91,
            "unit":"mg"},{"name":"Folate","amount":16.38,"unit":"µg"},{"name":"Sugar","amount":7.28,"unit":"g"},
            {"name":"Magnesium","amount":18.2,"unit":"mg"},{"name":"Zinc","amount":0.13,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.15,"unit":"g"},{"name":"Vitamin B6","amount":0.15,"unit":"mg"},
            {"name":"Vitamin E","amount":0.69,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.11,"unit":"mg"},{"name":"Vitamin A","amount":1168.44,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.05,"unit":"g"},{"name":"Manganese","amount":0.18,"unit":"mg"},
            {"name":"Vitamin C","amount":42.59,"unit":"mg"},{"name":"Selenium","amount":0.73,"unit":"µg"},
            {"name":"Net Carbohydrates","amount":7.28,"unit":"g"},{"name":"Vitamin B5","amount":0.91,"unit":"mg"},
            {"name":"Vitamin K","amount":18.38,"unit":"µg"},{"name":"Saturated Fat","amount":0.05,"unit":"g"},
            {"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.07,"unit":"mg"},
            {"name":"Fiber","amount":2.0,"unit":"g"},{"name":"Iron","amount":0.93,"unit":"mg"},{"name":"Caffeine",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":50.96,"unit":"mg"},{"name":"Carbohydrates",
            "amount":9.28,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":23.66,
            "unit":"mg"},{"name":"Calcium","amount":23.66,"unit":"mg"},{"name":"Potassium","amount":371.28,
            "unit":"mg"},{"name":"Choline","amount":15.65,"unit":"mg"},{"name":"Calories","amount":41.86,
            "unit":"kcal"},{"name":"Copper","amount":0.16,"unit":"mg"},{"name":"Folic Acid","amount":0.0,
            "unit":"µg"},{"name":"Protein","amount":2.18,"unit":"g"},{"name":"Fat","amount":0.36,"unit":"g"}]},
            {"id":4053,"name":"olive oil","amount":1.0,"unit":"tablespoon","nutrients":[{"name":"Vitamin B3",
            "amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.0,
            "unit":"g"},{"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},
            {"name":"Poly Unsaturated Fat","amount":1.47,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},
            {"name":"Vitamin E","amount":2.02,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":10.22,"unit":"g"},{"name":"Manganese","amount":0.0,"unit":"mg"},
            {"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":0.0,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            K","amount":8.43,"unit":"µg"},{"name":"Saturated Fat","amount":1.93,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,
            "unit":"g"},{"name":"Iron","amount":0.08,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":0.0,"unit":"mg"},{"name":"Carbohydrates","amount":0.0,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.28,"unit":"mg"},
            {"name":"Calcium","amount":0.14,"unit":"mg"},{"name":"Potassium","amount":0.14,"unit":"mg"},
            {"name":"Choline","amount":0.04,"unit":"mg"},{"name":"Calories","amount":123.76,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":14.0,"unit":"g"}]},{"id":10211111,
            "name":"sumac","amount":1.0,"unit":"teaspoon","nutrients":[{"name":"Vitamin B3","amount":0.0,
            "unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.0,"unit":"g"},
            {"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,"unit":"mg"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Trans Fat","amount":0.0,"unit":"g"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.0,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.0,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,
            "unit":"mg"},{"name":"Carbohydrates","amount":0.0,"unit":"g"},{"name":"Sodium","amount":0.0,"unit":"mg"},
            {"name":"Calcium","amount":0.0,"unit":"mg"},{"name":"Potassium","amount":0.0,"unit":"mg"},
            {"name":"Calories","amount":0.0,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},
            {"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]},{"id":2064,
            "name":"mint leaves","amount":1.0,"unit":"handful","nutrients":[{"name":"Vitamin B3","amount":0.07,
            "unit":"mg"},{"name":"Folate","amount":4.56,"unit":"µg"},{"name":"Magnesium","amount":3.2,"unit":"mg"},
            {"name":"Zinc","amount":0.04,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.02,"unit":"g"},
            {"name":"Vitamin B6","amount":0.01,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":169.92,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.05,"unit":"mg"},
            {"name":"Vitamin C","amount":1.27,"unit":"mg"},{"name":"Net Carbohydrates","amount":0.28,"unit":"g"},
            {"name":"Vitamin B5","amount":0.01,"unit":"mg"},{"name":"Saturated Fat","amount":0.01,"unit":"g"},
            {"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.32,"unit":"g"},{"name":"Iron",
            "amount":0.2,"unit":"mg"},{"name":"Phosphorus","amount":2.92,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.6,"unit":"g"},{"name":"Sodium","amount":1.24,"unit":"mg"},{"name":"Calcium","amount":9.72,
            "unit":"mg"},{"name":"Potassium","amount":22.76,"unit":"mg"},{"name":"Calories","amount":2.8,
            "unit":"kcal"},{"name":"Copper","amount":0.01,"unit":"mg"},{"name":"Folic Acid","amount":0.0,
            "unit":"µg"},{"name":"Protein","amount":0.15,"unit":"g"},{"name":"Fat","amount":0.04,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":5.23,"percentFat":72.63,"percentCarbs":22.14},"weightPerServing":{
            "amount":202,"unit":"g"}},"summary":"Green Tomato Salad might be a good recipe to expand your side dish 
            collection. This recipe serves 1 and costs 90 cents per serving. One serving contains <b>168 
            calories</b>, <b>2g of protein</b>, and <b>14g of fat</b>. From preparation to the plate, this recipe 
            takes roughly <b>roughly 45 minutes</b>. 1 person has made this recipe and would make it again. This 
            recipe from Foodista requires tomato, olive oil, sumac powder, and an of sage and mint leaves. It is a 
            good option if you're following a <b>gluten free, dairy free, paleolithic, and lacto ovo vegetarian</b> 
            diet. Taking all factors into account, this recipe <b>earns a spoonacular score of 78%</b>, 
            which is good. <a href=\"https://spoonacular.com/recipes/green-bean-and-tomato-salad-with-roasted-tomato
            -dressing-99198\">Green Bean-and-Tomato Salad with Roasted-Tomato Dressing</a>, 
            <a href=\"https://spoonacular.com/recipes/green-and-red-tomato-salad-306928\">Green and Red Tomato 
            Salad</a>, and <a href=\"https://spoonacular.com/recipes/tomato-green-bean-salad-444465\">Tomato-Green 
            Bean Salad</a> are very similar to this recipe.","cuisines":[],"dishTypes":["side dish"],"diets":["gluten 
            free","dairy free","paleolithic","lacto ovo vegetarian","primal","fodmap friendly","vegan"],"occasions":[
            ],"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Slice the tomato into thin round 
            discs.","ingredients":[{"id":11529,"name":"tomato","localizedName":"tomato","image":"tomato.png"}],
            "equipment":[]},{"number":2,"step":"Roll the mint and sage leaves into a tight ball and then chop it up 
            finely.","ingredients":[{"id":99226,"name":"sage","localizedName":"sage","image":"fresh-sage.png"},
            {"id":2064,"name":"mint","localizedName":"mint","image":"mint.jpg"},{"id":0,"name":"roll",
            "localizedName":"roll","image":"dinner-yeast-rolls.jpg"}],"equipment":[]},{"number":3,"step":"Add to the 
            olive oil and sumac to make a dressing.","ingredients":[{"id":4053,"name":"olive oil",
            "localizedName":"olive oil","image":"olive-oil.jpg"},{"id":10211111,"name":"sumac",
            "localizedName":"sumac","image":"dried-sumac.jpg"}],"equipment":[]},{"number":4,"step":"Drizzle over the 
            tomato slices","ingredients":[{"id":10511529,"name":"tomato slices","localizedName":"tomato slices",
            "image":"sliced-tomato.jpg"}],"equipment":[]}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/green-tomato-salad-645555","usedIngredientCount":1,
            "missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":10211111,"amount":1.0,"unit":"teaspoon",
            "unitLong":"teaspoon","unitShort":"tsp","aisle":"Ethnic Foods;Spices and Seasonings","name":"sumac",
            "original":"1 teaspoon of sumac powder","originalName":"sumac powder","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/dried-sumac.jpg"},{"id":2064,"amount":1.0,
            "unit":"handful","unitLong":"handful","unitShort":"handful","aisle":"Produce;Spices and Seasonings",
            "name":"mint leaves","original":"A handful of sage and mint leaves, finely chopped","originalName":"A of 
            sage and mint leaves, finely chopped","meta":["finely chopped"],"extendedName":"fresh mint leaves",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/mint.jpg"}],"usedIngredients":[{"id":11527,
            "amount":1.0,"unit":"large","unitLong":"large","unitShort":"large","aisle":"Produce","name":"green tomato","original":"1 large green tomato","originalName":"green tomato","meta":["green"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/green-tomato.png"}],"unusedIngredients":[]},
            {"vegetarian":true,"vegan":false,"glutenFree":true,"dairyFree":false,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":11,"gaps":"GAPS_FULL",
            "lowFodmap":false,"aggregateLikes":0,"spoonacularScore":37.0,"healthScore":5.0,
            "creditsText":"coffeebean","license":"spoonacular's terms","sourceName":"spoonacular",
            "pricePerServing":209.17,"extendedIngredients":[{"id":10011531,"aisle":"Canned and Jarred",
            "image":"tomatoes-canned.png","consistency":"solid","name":"tomatoes","nameClean":"canned whole 
            tomatoes","original":"28 ounces canned whole tomatoes","originalName":"canned whole tomatoes",
            "amount":28.0,"unit":"ounces","meta":["whole","canned"],"measures":{"us":{"amount":28.0,"unitShort":"oz",
            "unitLong":"ounces"},"metric":{"amount":793.787,"unitShort":"g","unitLong":"grams"}}},{"id":1001,
            "aisle":"Milk, Eggs, Other Dairy","image":"butter-sliced.jpg","consistency":"solid","name":"butter",
            "nameClean":"butter","original":"4 tablespoons butter","originalName":"butter","amount":4.0,
            "unit":"tablespoons","meta":[],"measures":{"us":{"amount":4.0,"unitShort":"Tbsps","unitLong":"Tbsps"},
            "metric":{"amount":4.0,"unitShort":"Tbsps","unitLong":"Tbsps"}}},{"id":11282,"aisle":"Produce",
            "image":"brown-onion.png","consistency":"solid","name":"onion","nameClean":"onion","original":"1 onion",
            "originalName":"onion","amount":1.0,"unit":"","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"",
            "unitLong":""},"metric":{"amount":1.0,"unitShort":"","unitLong":""}}},{"id":6615,"aisle":"Canned and 
            Jarred","image":"chicken-broth.png","consistency":"liquid","name":"vegetable broth",
            "nameClean":"vegetable stock","original":"1.5 cups vegetable broth","originalName":"vegetable broth",
            "amount":1.5,"unit":"cups","meta":[],"measures":{"us":{"amount":1.5,"unitShort":"cups",
            "unitLong":"cups"},"metric":{"amount":354.882,"unitShort":"ml","unitLong":"milliliters"}}}],"id":1674265,
            "title":"Easy Tomato Soup","author":"coffeebean","readyInMinutes":45,"servings":2,
            "sourceUrl":"https://spoonacular.com/site-1634294482382",
            "image":"https://spoonacular.com/recipeImages/1674265-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":299.04,"unit":"kcal","percentOfDailyNeeds":14.95},{"name":"Fat",
            "amount":23.28,"unit":"g","percentOfDailyNeeds":35.81},{"name":"Saturated Fat","amount":14.49,"unit":"g",
            "percentOfDailyNeeds":90.54},{"name":"Carbohydrates","amount":23.29,"unit":"g",
            "percentOfDailyNeeds":7.76},{"name":"Net Carbohydrates","amount":18.38,"unit":"g",
            "percentOfDailyNeeds":6.68},{"name":"Sugar","amount":13.29,"unit":"g","percentOfDailyNeeds":14.77},
            {"name":"Cholesterol","amount":60.2,"unit":"mg","percentOfDailyNeeds":20.07},{"name":"Sodium",
            "amount":1454.8,"unit":"mg","percentOfDailyNeeds":63.25},{"name":"Protein","amount":3.94,"unit":"g",
            "percentOfDailyNeeds":7.88},{"name":"Vitamin C","amount":40.98,"unit":"mg","percentOfDailyNeeds":49.67},
            {"name":"Vitamin A","amount":1540.6,"unit":"IU","percentOfDailyNeeds":30.81},{"name":"Vitamin B6",
            "amount":0.51,"unit":"mg","percentOfDailyNeeds":25.37},{"name":"Potassium","amount":833.18,"unit":"mg",
            "percentOfDailyNeeds":23.81},{"name":"Vitamin E","amount":3.36,"unit":"mg","percentOfDailyNeeds":22.4},
            {"name":"Iron","amount":3.97,"unit":"mg","percentOfDailyNeeds":22.06},{"name":"Fiber","amount":4.9,
            "unit":"g","percentOfDailyNeeds":19.62},{"name":"Manganese","amount":0.38,"unit":"mg",
            "percentOfDailyNeeds":18.83},{"name":"Copper","amount":0.3,"unit":"mg","percentOfDailyNeeds":14.77},
            {"name":"Vitamin B3","amount":2.9,"unit":"mg","percentOfDailyNeeds":14.51},{"name":"Vitamin B2",
            "amount":0.24,"unit":"mg","percentOfDailyNeeds":14.27},{"name":"Calcium","amount":142.41,"unit":"mg",
            "percentOfDailyNeeds":14.24},{"name":"Vitamin B1","amount":0.21,"unit":"mg","percentOfDailyNeeds":13.69},
            {"name":"Vitamin K","amount":13.69,"unit":"µg","percentOfDailyNeeds":13.04},{"name":"Magnesium",
            "amount":49.72,"unit":"mg","percentOfDailyNeeds":12.43},{"name":"Folate","amount":43.04,"unit":"µg",
            "percentOfDailyNeeds":10.76},{"name":"Phosphorus","amount":98.08,"unit":"mg","percentOfDailyNeeds":9.81},
            {"name":"Vitamin B5","amount":0.57,"unit":"mg","percentOfDailyNeeds":5.67},{"name":"Zinc","amount":0.67,
            "unit":"mg","percentOfDailyNeeds":4.5},{"name":"Selenium","amount":0.95,"unit":"µg",
            "percentOfDailyNeeds":1.36}],"properties":[{"name":"Glycemic Index","amount":61.0,"unit":""},
            {"name":"Glycemic Load","amount":2.16,"unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,
            "unit":""},{"name":"Petunidin","amount":0.0,"unit":""},{"name":"Delphinidin","amount":0.0,"unit":""},
            {"name":"Malvidin","amount":0.0,"unit":""},{"name":"Pelargonidin","amount":0.0,"unit":""},
            {"name":"Peonidin","amount":0.0,"unit":""},{"name":"Catechin","amount":0.0,"unit":"mg"},
            {"name":"Epigallocatechin","amount":0.0,"unit":"mg"},{"name":"Epicatechin","amount":0.0,"unit":"mg"},
            {"name":"Epicatechin 3-gallate","amount":0.0,"unit":"mg"},{"name":"Epigallocatechin 3-gallate",
            "amount":0.0,"unit":"mg"},{"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins",
            "amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},{"name":"Hesperetin","amount":0.0,
            "unit":""},{"name":"Naringenin","amount":0.0,"unit":""},{"name":"Apigenin","amount":0.05,"unit":"mg"},
            {"name":"Luteolin","amount":0.09,"unit":"mg"},{"name":"Isorhamnetin","amount":2.76,"unit":"mg"},
            {"name":"Kaempferol","amount":0.4,"unit":"mg"},{"name":"Myricetin","amount":0.14,"unit":"mg"},
            {"name":"Quercetin","amount":13.15,"unit":"mg"},{"name":"Theaflavin-3,3'-digallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate",
            "amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,"unit":"mg"}],"ingredients":[{"id":10011531,
            "name":"tomatoes","amount":14.0,"unit":"ounces","nutrients":[{"name":"Vitamin B3","amount":2.83,
            "unit":"mg"},{"name":"Folate","amount":31.75,"unit":"µg"},{"name":"Sugar","amount":9.45,"unit":"g"},
            {"name":"Magnesium","amount":43.66,"unit":"mg"},{"name":"Zinc","amount":0.56,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.21,"unit":"g"},{"name":"Vitamin B6","amount":0.44,"unit":"mg"},
            {"name":"Vitamin E","amount":2.7,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.18,"unit":"mg"},{"name":"Vitamin A","amount":464.37,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.08,"unit":"g"},{"name":"Fluoride","amount":20.24,"unit":"mg"},
            {"name":"Manganese","amount":0.31,"unit":"mg"},{"name":"Vitamin C","amount":36.91,"unit":"mg"},
            {"name":"Selenium","amount":0.4,"unit":"µg"},{"name":"Net Carbohydrates","amount":11.91,"unit":"g"},
            {"name":"Vitamin B5","amount":0.47,"unit":"mg"},{"name":"Vitamin K","amount":11.51,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.07,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.22,"unit":"mg"},{"name":"Fiber","amount":3.97,"unit":"g"},{"name":"Iron",
            "amount":3.85,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":75.41,"unit":"mg"},{"name":"Carbohydrates","amount":15.88,"unit":"g"},{"name":"Lycopene",
            "amount":10982.04,"unit":"µg"},{"name":"Sodium","amount":567.56,"unit":"mg"},{"name":"Calcium",
            "amount":123.04,"unit":"mg"},{"name":"Potassium","amount":746.16,"unit":"mg"},{"name":"Choline",
            "amount":27.78,"unit":"mg"},{"name":"Calories","amount":67.47,"unit":"kcal"},{"name":"Copper",
            "amount":0.27,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":3.1,
            "unit":"g"},{"name":"Fat","amount":0.52,"unit":"g"}]},{"id":1001,"name":"butter","amount":2.0,
            "unit":"tablespoons","nutrients":[{"name":"Vitamin B3","amount":0.01,"unit":"mg"},{"name":"Folate",
            "amount":0.84,"unit":"µg"},{"name":"Sugar","amount":0.02,"unit":"g"},{"name":"Magnesium","amount":0.56,
            "unit":"mg"},{"name":"Zinc","amount":0.03,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.85,
            "unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin E","amount":0.65,
            "unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,
            "unit":"mg"},{"name":"Vitamin A","amount":699.72,"unit":"IU"},{"name":"Vitamin B12","amount":0.05,
            "unit":"µg"},{"name":"Cholesterol","amount":60.2,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":5.88,"unit":"g"},{"name":"Fluoride","amount":0.78,"unit":"mg"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Trans Fat","amount":0.92,"unit":"g"},
            {"name":"Selenium","amount":0.28,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.02,"unit":"g"},
            {"name":"Vitamin B5","amount":0.03,"unit":"mg"},{"name":"Vitamin K","amount":1.96,"unit":"µg"},
            {"name":"Saturated Fat","amount":14.39,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.01,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":6.72,"unit":"mg"},{"name":"Carbohydrates","amount":0.02,"unit":"g"},{"name":"Lycopene",
            "amount":0.0,"unit":"µg"},{"name":"Sodium","amount":180.04,"unit":"mg"},{"name":"Calcium","amount":6.72,
            "unit":"mg"},{"name":"Potassium","amount":6.72,"unit":"mg"},{"name":"Choline","amount":5.26,"unit":"mg"},
            {"name":"Calories","amount":200.76,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.24,"unit":"g"},{"name":"Fat",
            "amount":22.71,"unit":"g"}]},{"id":11282,"name":"onion","amount":0.5,"unit":"","nutrients":[{
            "name":"Vitamin B3","amount":0.06,"unit":"mg"},{"name":"Folate","amount":10.45,"unit":"µg"},
            {"name":"Sugar","amount":2.33,"unit":"g"},{"name":"Magnesium","amount":5.5,"unit":"mg"},{"name":"Zinc",
            "amount":0.09,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.01,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.07,"unit":"mg"},{"name":"Vitamin E","amount":0.01,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.03,"unit":"mg"},{"name":"Vitamin A",
            "amount":1.1,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.01,"unit":"g"},{"name":"Fluoride",
            "amount":0.61,"unit":"mg"},{"name":"Manganese","amount":0.07,"unit":"mg"},{"name":"Vitamin C",
            "amount":4.07,"unit":"mg"},{"name":"Selenium","amount":0.28,"unit":"µg"},{"name":"Net Carbohydrates",
            "amount":4.2,"unit":"g"},{"name":"Vitamin B5","amount":0.07,"unit":"mg"},{"name":"Vitamin K",
            "amount":0.22,"unit":"µg"},{"name":"Saturated Fat","amount":0.02,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.94,
            "unit":"g"},{"name":"Iron","amount":0.12,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":15.95,"unit":"mg"},{"name":"Carbohydrates","amount":5.14,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":2.2,"unit":"mg"},
            {"name":"Calcium","amount":12.65,"unit":"mg"},{"name":"Potassium","amount":80.3,"unit":"mg"},
            {"name":"Choline","amount":3.36,"unit":"mg"},{"name":"Calories","amount":22.0,"unit":"kcal"},
            {"name":"Copper","amount":0.02,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.61,"unit":"g"},{"name":"Fat","amount":0.06,"unit":"g"}]},{"id":6615,
            "name":"vegetable broth","amount":0.75,"unit":"cups","nutrients":[{"name":"Sugar","amount":1.5,
            "unit":"g"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":0.0,"unit":"mg"},
            {"name":"Vitamin A","amount":375.41,"unit":"IU"},{"name":"Carbohydrates","amount":2.26,"unit":"g"},
            {"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Sodium","amount":705.0,"unit":"mg"},
            {"name":"Calcium","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Trans 
            Fat","amount":0.0,"unit":"g"},{"name":"Calories","amount":8.81,"unit":"kcal"},{"name":"Net 
            Carbohydrates","amount":2.26,"unit":"g"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},
            {"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]}],"caloricBreakdown":{
            "percentProtein":4.95,"percentFat":65.8,"percentCarbs":29.25},"weightPerServing":{"amount":656,
            "unit":"g"}},"summary":"Easy Tomato Soup is a <b>gluten free, lacto ovo vegetarian, and primal</b> recipe 
            with 2 servings. One serving contains <b>299 calories</b>, <b>4g of protein</b>, and <b>23g of fat</b>. 
            For <b>$2.09 per serving</b>, this recipe <b>covers 14%</b> of your daily requirements of vitamins and 
            minerals. From preparation to the plate, this recipe takes around <b>45 minutes</b>. It can be enjoyed 
            any time, but it is especially good for <b>Autumn</b>. A mixture of tomatoes, butter, onion, 
            and a handful of other ingredients are all it takes to make this recipe so flavorful. It is brought to 
            you by spoonacular user <a href=\"/profile/coffeebean\">coffeebean</a>. If you like this recipe, 
            take a look at these similar recipes: <a 
            href=\"https://spoonacular.com/recipes/tomato-soup-easy-vegan-soup-s-564679\">Tomato Soup | Easy Vegan 
            Soup s</a>, <a href=\"https://spoonacular.com/recipes/tomato-soup-easy-vegan-soup-s-1359295\">Tomato Soup 
            | Easy Vegan Soup s</a>, and <a href=\"https://spoonacular.com/recipes/easy-tomato-soup-597165\">Easy 
            Tomato Soup</a>.","cuisines":[],"dishTypes":["antipasti","soup","starter","snack","appetizer",
            "antipasto","hor d'oeuvre"],"diets":["gluten free","lacto ovo vegetarian","primal"],"occasions":["fall",
            "winter"],"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"In a medium pot, melt butter 
            over medium heat.","ingredients":[{"id":1001,"name":"butter","localizedName":"butter",
            "image":"butter-sliced.jpg"}],"equipment":[{"id":404752,"name":"pot","localizedName":"pot",
            "image":"stock-pot.jpg"}]},{"number":2,"step":"Cut onion into 4 wedges and add to the pot along with the 
            canned tomatoes and vegetable broth. Bring to a simmer. Simmer, uncovered, for about 40 minutes. Stir 
            occasionally.Blend the soup with an immersion blender and season to taste.If you happen to have fresh 
            basil on hand, throw in a handful before blending.","ingredients":[{"id":10011693,"name":"canned 
            tomatoes","localizedName":"canned tomatoes","image":"tomatoes-canned.png"},{"id":6615,"name":"vegetable 
            broth","localizedName":"vegetable broth","image":"chicken-broth.png"},{"id":2044,"name":"fresh basil",
            "localizedName":"fresh basil","image":"fresh-basil.jpg"},{"id":11282,"name":"onion",
            "localizedName":"onion","image":"brown-onion.png"},{"id":0,"name":"soup","localizedName":"soup",
            "image":""}],"equipment":[{"id":404776,"name":"immersion blender","localizedName":"immersion blender",
            "image":"immersion-blender.png"},{"id":404752,"name":"pot","localizedName":"pot",
            "image":"stock-pot.jpg"}],"length":{"number":40,"unit":"minutes"}}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/easy-tomato-soup-1674265","usedIngredientCount":1,
            "missedIngredientCount":3,"likes":0,"missedIngredients":[{"id":1001,"amount":4.0,"unit":"tablespoons",
            "unitLong":"tablespoons","unitShort":"Tbsp","aisle":"Milk, Eggs, Other Dairy","name":"butter",
            "original":"4 tablespoons butter","originalName":"butter","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"},{"id":11282,"amount":1.0,
            "unit":"","unitLong":"","unitShort":"","aisle":"Produce","name":"onion","original":"1 onion",
            "originalName":"onion","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/brown-onion.png"},{"id":6615,"amount":1.5,
            "unit":"cups","unitLong":"cups","unitShort":"cup","aisle":"Canned and Jarred","name":"vegetable broth",
            "original":"1.5 cups vegetable broth","originalName":"vegetable broth","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/chicken-broth.png"}],"usedIngredients":[{
            "id":10011531,"amount":28.0,"unit":"ounces","unitLong":"ounces","unitShort":"oz","aisle":"Canned and 
            Jarred","name":"tomatoes","original":"28 ounces canned whole tomatoes","originalName":"canned whole 
            tomatoes","meta":["whole","canned"],"extendedName":"canned whole tomatoes",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/tomatoes-canned.png"}],"unusedIngredients":[]},
            {"vegetarian":true,"vegan":false,"glutenFree":true,"dairyFree":false,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":15,"gaps":"no","lowFodmap":false,
            "aggregateLikes":1,"spoonacularScore":77.0,"healthScore":29.0,"creditsText":"Foodista.com – The Cooking 
            Encyclopedia Everyone Can Edit","license":"CC BY 3.0","sourceName":"Foodista","pricePerServing":563.28,
            "extendedIngredients":[{"id":1159,"aisle":"Cheese","image":"goat-cheese.jpg","consistency":"solid",
            "name":"goat cheese","nameClean":"goat cheese","original":"1 package (5.3 oz) Fresh Goat Cheese, 
            such as Chavrie","originalName":"package Fresh Goat Cheese, such as Chavrie","amount":5.3,"unit":"oz",
            "meta":["fresh"," such as chavrie"],"measures":{"us":{"amount":5.3,"unitShort":"oz","unitLong":"ounces"},
            "metric":{"amount":150.252,"unitShort":"g","unitLong":"grams"}}},{"id":10011693,"aisle":"Canned and 
            Jarred","image":"tomatoes-canned.png","consistency":"solid","name":"canned tomatoes","nameClean":"canned 
            tomatoes","original":"8 oz. can diced tomatoes, drained","originalName":"diced tomatoes, drained",
            "amount":8.0,"unit":"oz","meta":["diced","drained","canned"],"measures":{"us":{"amount":8.0,
            "unitShort":"oz","unitLong":"ounces"},"metric":{"amount":226.796,"unitShort":"g","unitLong":"grams"}}},
            {"id":11979,"aisle":"Canned and Jarred;Produce;Ethnic Foods","image":"jalapeno-pepper.png",
            "consistency":"solid","name":"jalapeno pepper","nameClean":"jalapeno pepper","original":"1 ea. jalapeno 
            pepper diced","originalName":"ea. jalapeno pepper diced","amount":1.0,"unit":"","meta":["diced"],
            "measures":{"us":{"amount":1.0,"unitShort":"","unitLong":""},"metric":{"amount":1.0,"unitShort":"",
            "unitLong":""}}},{"id":6168,"aisle":"Condiments","image":"hot-sauce-or-tabasco.png",
            "consistency":"liquid","name":"hot sauce","nameClean":"hot sauce","original":"2 teaspoons hot sauce",
            "originalName":"hot sauce","amount":2.0,"unit":"teaspoons","meta":[],"measures":{"us":{"amount":2.0,
            "unitShort":"tsps","unitLong":"teaspoons"},"metric":{"amount":2.0,"unitShort":"tsps",
            "unitLong":"teaspoons"}}}],"id":648368,"title":"Jalapeno Queso With Goat Cheese","readyInMinutes":45,
            "servings":1,"sourceUrl":"https://www.foodista.com/recipe/H6XM7BBC/jalapeno-queso-with-goat-cheese",
            "image":"https://spoonacular.com/recipeImages/648368-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":474.18,"unit":"kcal","percentOfDailyNeeds":23.71},{"name":"Fat",
            "amount":32.39,"unit":"g","percentOfDailyNeeds":49.83},{"name":"Saturated Fat","amount":22.01,"unit":"g",
            "percentOfDailyNeeds":137.54},{"name":"Carbohydrates","amount":17.58,"unit":"g",
            "percentOfDailyNeeds":5.86},{"name":"Net Carbohydrates","amount":12.86,"unit":"g",
            "percentOfDailyNeeds":4.68},{"name":"Sugar","amount":11.99,"unit":"g","percentOfDailyNeeds":13.33},
            {"name":"Cholesterol","amount":69.12,"unit":"mg","percentOfDailyNeeds":23.04},{"name":"Sodium",
            "amount":1064.16,"unit":"mg","percentOfDailyNeeds":46.27},{"name":"Protein","amount":31.71,"unit":"g",
            "percentOfDailyNeeds":63.43},{"name":"Copper","amount":1.52,"unit":"mg","percentOfDailyNeeds":76.18},
            {"name":"Vitamin C","amount":43.45,"unit":"mg","percentOfDailyNeeds":52.67},{"name":"Phosphorus",
            "amount":461.74,"unit":"mg","percentOfDailyNeeds":46.17},{"name":"Vitamin A","amount":2203.59,
            "unit":"IU","percentOfDailyNeeds":44.07},{"name":"Vitamin B2","amount":0.71,"unit":"mg",
            "percentOfDailyNeeds":41.49},{"name":"Vitamin B6","amount":0.79,"unit":"mg","percentOfDailyNeeds":39.35},
            {"name":"Iron","amount":5.88,"unit":"mg","percentOfDailyNeeds":32.65},{"name":"Manganese","amount":0.58,
            "unit":"mg","percentOfDailyNeeds":29.14},{"name":"Calcium","amount":289.78,"unit":"mg",
            "percentOfDailyNeeds":28.98},{"name":"Vitamin E","amount":3.62,"unit":"mg","percentOfDailyNeeds":24.11},
            {"name":"Potassium","amount":749.82,"unit":"mg","percentOfDailyNeeds":21.42},{"name":"Vitamin B1",
            "amount":0.28,"unit":"mg","percentOfDailyNeeds":18.92},{"name":"Fiber","amount":4.73,"unit":"g",
            "percentOfDailyNeeds":18.9},{"name":"Vitamin B3","amount":3.62,"unit":"mg","percentOfDailyNeeds":18.09},
            {"name":"Magnesium","amount":71.9,"unit":"mg","percentOfDailyNeeds":17.97},{"name":"Vitamin B5",
            "amount":1.71,"unit":"mg","percentOfDailyNeeds":17.05},{"name":"Vitamin K","amount":17.51,"unit":"µg",
            "percentOfDailyNeeds":16.67},{"name":"Zinc","amount":2.02,"unit":"mg","percentOfDailyNeeds":13.49},
            {"name":"Folate","amount":51.77,"unit":"µg","percentOfDailyNeeds":12.94},{"name":"Selenium",
            "amount":5.62,"unit":"µg","percentOfDailyNeeds":8.03},{"name":"Vitamin B12","amount":0.29,"unit":"µg",
            "percentOfDailyNeeds":4.76},{"name":"Vitamin D","amount":0.6,"unit":"µg","percentOfDailyNeeds":4.01}],
            "properties":[{"name":"Glycemic Index","amount":70.0,"unit":""},{"name":"Glycemic Load","amount":4.81,
            "unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,
            "unit":""},{"name":"Delphinidin","amount":0.0,"unit":""},{"name":"Malvidin","amount":0.0,"unit":""},
            {"name":"Pelargonidin","amount":0.0,"unit":""},{"name":"Peonidin","amount":0.0,"unit":""},
            {"name":"Catechin","amount":0.0,"unit":""},{"name":"Epigallocatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin","amount":0.0,"unit":""},{"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},
            {"name":"Epigallocatechin 3-gallate","amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,
            "unit":""},{"name":"Thearubigins","amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},
            {"name":"Hesperetin","amount":0.0,"unit":""},{"name":"Naringenin","amount":0.0,"unit":""},
            {"name":"Apigenin","amount":0.0,"unit":""},{"name":"Luteolin","amount":0.19,"unit":"mg"},
            {"name":"Isorhamnetin","amount":0.0,"unit":""},{"name":"Kaempferol","amount":0.0,"unit":""},
            {"name":"Myricetin","amount":0.0,"unit":""},{"name":"Quercetin","amount":0.71,"unit":"mg"},
            {"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,
            "unit":""}],"ingredients":[{"id":1159,"name":"goat cheese","amount":5.3,"unit":"oz","nutrients":[{
            "name":"Vitamin B3","amount":0.65,"unit":"mg"},{"name":"Folate","amount":18.03,"unit":"µg"},
            {"name":"Sugar","amount":1.34,"unit":"g"},{"name":"Magnesium","amount":24.04,"unit":"mg"},{"name":"Zinc",
            "amount":1.38,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.75,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.38,"unit":"mg"},{"name":"Vitamin E","amount":0.27,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.6,"unit":"µg"},{"name":"Vitamin B1","amount":0.11,"unit":"mg"},{"name":"Vitamin A",
            "amount":1552.1,"unit":"IU"},{"name":"Vitamin B12","amount":0.29,"unit":"µg"},{"name":"Cholesterol",
            "amount":69.12,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":7.22,"unit":"g"},{"name":"Manganese",
            "amount":0.15,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":4.21,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.0,"unit":"g"},{"name":"Vitamin B5",
            "amount":1.02,"unit":"mg"},{"name":"Vitamin K","amount":2.7,"unit":"µg"},{"name":"Saturated Fat",
            "amount":21.9,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.57,
            "unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":2.85,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":384.65,"unit":"mg"},
            {"name":"Carbohydrates","amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},
            {"name":"Sodium","amount":552.93,"unit":"mg"},{"name":"Calcium","amount":210.35,"unit":"mg"},
            {"name":"Potassium","amount":39.07,"unit":"mg"},{"name":"Choline","amount":23.14,"unit":"mg"},
            {"name":"Calories","amount":396.67,"unit":"kcal"},{"name":"Copper","amount":1.1,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":27.83,"unit":"g"},
            {"name":"Fat","amount":31.67,"unit":"g"}]},{"id":10011693,"name":"canned tomatoes","amount":8.0,
            "unit":"oz","nutrients":[{"name":"Vitamin B3","amount":2.77,"unit":"mg"},{"name":"Folate","amount":29.48,
            "unit":"µg"},{"name":"Sugar","amount":9.98,"unit":"g"},{"name":"Magnesium","amount":45.36,"unit":"mg"},
            {"name":"Zinc","amount":0.61,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.26,"unit":"g"},
            {"name":"Vitamin B6","amount":0.34,"unit":"mg"},{"name":"Vitamin E","amount":2.83,"unit":"mg"},
            {"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.17,"unit":"mg"},
            {"name":"Vitamin A","amount":487.61,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},
            {"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.1,"unit":"g"},
            {"name":"Manganese","amount":0.42,"unit":"mg"},{"name":"Vitamin C","amount":20.87,"unit":"mg"},
            {"name":"Selenium","amount":1.36,"unit":"µg"},{"name":"Net Carbohydrates","amount":12.22,"unit":"g"},
            {"name":"Vitamin B5","amount":0.63,"unit":"mg"},{"name":"Vitamin K","amount":12.02,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.09,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.12,"unit":"mg"},{"name":"Fiber","amount":4.31,"unit":"g"},{"name":"Iron",
            "amount":2.95,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":72.57,"unit":"mg"},{"name":"Carbohydrates","amount":16.53,"unit":"g"},{"name":"Lycopene",
            "amount":11580.2,"unit":"µg"},{"name":"Sodium","amount":299.37,"unit":"mg"},{"name":"Calcium",
            "amount":77.11,"unit":"mg"},{"name":"Potassium","amount":664.51,"unit":"mg"},{"name":"Choline",
            "amount":29.26,"unit":"mg"},{"name":"Calories","amount":72.57,"unit":"kcal"},{"name":"Copper",
            "amount":0.42,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein",
            "amount":3.72,"unit":"g"},{"name":"Fat","amount":0.64,"unit":"g"}]},{"id":11979,"name":"jalapeno pepper",
            "amount":1.0,"unit":"","nutrients":[{"name":"Vitamin B3","amount":0.18,"unit":"mg"},{"name":"Folate",
            "amount":3.78,"unit":"µg"},{"name":"Sugar","amount":0.58,"unit":"g"},{"name":"Magnesium","amount":2.1,
            "unit":"mg"},{"name":"Zinc","amount":0.02,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.02,
            "unit":"g"},{"name":"Vitamin B6","amount":0.06,"unit":"mg"},{"name":"Vitamin E","amount":0.5,
            "unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.01,
            "unit":"mg"},{"name":"Vitamin A","amount":150.92,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,
            "unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,
            "unit":"g"},{"name":"Manganese","amount":0.01,"unit":"mg"},{"name":"Vitamin C","amount":16.6,
            "unit":"mg"},{"name":"Trans Fat","amount":0.0,"unit":"g"},{"name":"Selenium","amount":0.06,"unit":"µg"},
            {"name":"Net Carbohydrates","amount":0.52,"unit":"g"},{"name":"Vitamin B5","amount":0.04,"unit":"mg"},
            {"name":"Vitamin K","amount":2.59,"unit":"µg"},{"name":"Saturated Fat","amount":0.01,"unit":"g"},
            {"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.01,"unit":"mg"},
            {"name":"Fiber","amount":0.39,"unit":"g"},{"name":"Iron","amount":0.04,"unit":"mg"},{"name":"Caffeine",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":3.64,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.91,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.42,
            "unit":"mg"},{"name":"Calcium","amount":1.68,"unit":"mg"},{"name":"Potassium","amount":34.72,
            "unit":"mg"},{"name":"Choline","amount":1.05,"unit":"mg"},{"name":"Calories","amount":4.06,
            "unit":"kcal"},{"name":"Copper","amount":0.01,"unit":"mg"},{"name":"Folic Acid","amount":0.0,
            "unit":"µg"},{"name":"Protein","amount":0.13,"unit":"g"},{"name":"Fat","amount":0.05,"unit":"g"}]},
            {"id":6168,"name":"hot sauce","amount":2.0,"unit":"teaspoons","nutrients":[{"name":"Vitamin B3",
            "amount":0.02,"unit":"mg"},{"name":"Folate","amount":0.48,"unit":"µg"},{"name":"Sugar","amount":0.1,
            "unit":"g"},{"name":"Magnesium","amount":0.4,"unit":"mg"},{"name":"Zinc","amount":0.01,"unit":"mg"},
            {"name":"Poly Unsaturated Fat","amount":0.02,"unit":"g"},{"name":"Vitamin B6","amount":0.01,"unit":"mg"},
            {"name":"Vitamin E","amount":0.01,"unit":"mg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},
            {"name":"Vitamin A","amount":12.96,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},
            {"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},
            {"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":5.98,"unit":"mg"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.12,"unit":"g"},
            {"name":"Vitamin B5","amount":0.01,"unit":"mg"},{"name":"Vitamin K","amount":0.19,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.01,"unit":"mg"},
            {"name":"Fiber","amount":0.02,"unit":"g"},{"name":"Iron","amount":0.04,"unit":"mg"},{"name":"Phosphorus",
            "amount":0.88,"unit":"mg"},{"name":"Carbohydrates","amount":0.14,"unit":"g"},{"name":"Lycopene",
            "amount":0.0,"unit":"µg"},{"name":"Sodium","amount":211.44,"unit":"mg"},{"name":"Calcium","amount":0.64,
            "unit":"mg"},{"name":"Potassium","amount":11.52,"unit":"mg"},{"name":"Calories","amount":0.88,
            "unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.04,"unit":"g"},{"name":"Fat","amount":0.03,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":25.96,"percentFat":59.65,"percentCarbs":14.39},"weightPerServing":{
            "amount":399,"unit":"g"}},"summary":"If you have approximately <b>around 45 minutes</b> to spend in the 
            kitchen, Jalapeno Queso With Goat Cheese might be a super <b>gluten free and lacto ovo vegetarian</b> 
            recipe to try. This recipe makes 1 servings with <b>474 calories</b>, <b>32g of protein</b>, and <b>32g 
            of fat</b> each. For <b>$5.63 per serving</b>, this recipe <b>covers 26%</b> of your daily requirements 
            of vitamins and minerals. Not a lot of people made this recipe, and 1 would say it hit the spot. Head to 
            the store and pick up hot sauce, canned tomatoes, ea. jalapeno pepper, and a few other things to make it 
            today. It is brought to you by Foodista. All things considered, we decided this recipe <b>deserves a 
            spoonacular score of 76%</b>. This score is solid. Similar recipes are <a 
            href=\"https://spoonacular.com/recipes/smokey-roasted-chicken-tacos-with-spicy-goat-cheese-queso-525564
            \">Smokey Roasted Chicken Tacos with Spicy Goat Cheese Queso</a>, 
            <a href=\"https://spoonacular.com/recipes/queso-de-cabra-con-tomate-goat-cheese-baked-in-tomato-sauce
            -108554\">Queso De Cabra Con Tomate (Goat Cheese Baked in Tomato Sauce)</a>, 
            and <a href=\"https://spoonacular.com/recipes/jalapeo-poppers-with-goat-cheese-and-bacon-83424\">Jalapeño 
            Poppers With Goat Cheese And Bacon</a>.","cuisines":[],"dishTypes":[],"diets":["gluten free","lacto ovo 
            vegetarian"],"occasions":[],"analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Mix all 
            ingredients in a glass bowl and slowly heat in the microwave until piping hot.","ingredients":[],
            "equipment":[{"id":404762,"name":"microwave","localizedName":"microwave","image":"microwave.jpg"},
            {"id":404783,"name":"bowl","localizedName":"bowl","image":"bowl.jpg"}]},{"number":2,"step":"Salt and 
            freshly ground black pepper to taste.","ingredients":[{"id":1002030,"name":"ground black pepper",
            "localizedName":"ground black pepper","image":"pepper.jpg"},{"id":2047,"name":"salt",
            "localizedName":"salt","image":"salt.jpg"}],"equipment":[]}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/jalapeno-queso-with-goat-cheese-648368",
            "usedIngredientCount":1,"missedIngredientCount":3,"likes":0,"missedIngredients":[{"id":1159,"amount":5.3,
            "unit":"oz","unitLong":"ounces","unitShort":"oz","aisle":"Cheese","name":"goat cheese","original":"1 
            package (5.3 oz) Fresh Goat Cheese, such as Chavrie","originalName":"package Fresh Goat Cheese, 
            such as Chavrie","meta":["fresh"," such as chavrie"],"extendedName":"fresh goat cheese",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/goat-cheese.jpg"},{"id":11979,"amount":1.0,
            "unit":"","unitLong":"","unitShort":"","aisle":"Canned and Jarred;Produce;Ethnic Foods","name":"jalapeno pepper","original":"1 ea. jalapeno pepper diced","originalName":"ea. jalapeno pepper diced",
            "meta":["diced"],"extendedName":"diced jalapeno pepper",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/jalapeno-pepper.png"},{"id":6168,"amount":2.0,
            "unit":"teaspoons","unitLong":"teaspoons","unitShort":"tsp","aisle":"Condiments","name":"hot sauce",
            "original":"2 teaspoons hot sauce","originalName":"hot sauce","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/hot-sauce-or-tabasco.png"}],"usedIngredients":[{
            "id":10011693,"amount":8.0,"unit":"oz","unitLong":"ounces","unitShort":"oz","aisle":"Canned and Jarred",
            "name":"canned tomatoes","original":"8 oz. can diced tomatoes, drained","originalName":"diced tomatoes, 
            drained","meta":["diced","drained","canned"],"extendedName":"diced canned tomatoes",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/tomatoes-canned.png"}],"unusedIngredients":[]},
            {"vegetarian":true,"vegan":false,"glutenFree":true,"dairyFree":false,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":4,"gaps":"GAPS_FULL",
            "lowFodmap":false,"aggregateLikes":5,"spoonacularScore":70.0,"healthScore":16.0,
            "creditsText":"Foodista.com – The Cooking Encyclopedia Everyone Can Edit","license":"CC BY 3.0",
            "sourceName":"Foodista","pricePerServing":113.27,"extendedIngredients":[{"id":11209,"aisle":"Produce",
            "image":"eggplant.png","consistency":"solid","name":"eggplant","nameClean":"eggplant","original":"1 large 
            round eggplant, washed, sliced into rounds","originalName":"round eggplant, washed, sliced into rounds",
            "amount":1.0,"unit":"large","meta":["washed","sliced into rounds"],"measures":{"us":{"amount":1.0,
            "unitShort":"large","unitLong":"large"},"metric":{"amount":1.0,"unitShort":"large","unitLong":"large"}}},
            {"id":11529,"aisle":"Produce","image":"tomato.png","consistency":"solid","name":"tomatoes",
            "nameClean":"tomato","original":"10 Tbs chopped tomatoes","originalName":"chopped tomatoes",
            "amount":10.0,"unit":"Tbs","meta":["chopped"],"measures":{"us":{"amount":10.0,"unitShort":"Tbs",
            "unitLong":"Tbs"},"metric":{"amount":10.0,"unitShort":"Tbs","unitLong":"Tbs"}}},{"id":1040,
            "aisle":"Cheese","image":"Swiss-cheese.jpg","consistency":"solid","name":"swiss cheese",
            "nameClean":"swiss cheese","original":"100g Swiss cheese, coarsely grated","originalName":"Swiss cheese, 
            coarsely grated","amount":100.0,"unit":"g","meta":["grated"],"measures":{"us":{"amount":3.527,
            "unitShort":"oz","unitLong":"ounces"},"metric":{"amount":100.0,"unitShort":"g","unitLong":"grams"}}},
            {"id":2044,"aisle":"Produce","image":"fresh-basil.jpg","consistency":"solid","name":"basil leaves",
            "nameClean":"fresh basil","original":"Basil and oregano leaves, fresh or dried","originalName":"Basil and 
            oregano , fresh or dried","amount":1.0,"unit":"leaves","meta":["fresh"],"measures":{"us":{"amount":1.0,
            "unitShort":"leaf","unitLong":"leave"},"metric":{"amount":1.0,"unitShort":"leaf","unitLong":"leave"}}}],
            "id":642303,"title":"Eggplant pizzette","readyInMinutes":45,"servings":3,
            "sourceUrl":"https://www.foodista.com/recipe/Z8BW2C8N/eggplant-pizzette",
            "image":"https://spoonacular.com/recipeImages/642303-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":178.07,"unit":"kcal","percentOfDailyNeeds":8.9},{"name":"Fat",
            "amount":10.71,"unit":"g","percentOfDailyNeeds":16.47},{"name":"Saturated Fat","amount":6.13,"unit":"g",
            "percentOfDailyNeeds":38.33},{"name":"Carbohydrates","amount":11.38,"unit":"g",
            "percentOfDailyNeeds":3.79},{"name":"Net Carbohydrates","amount":6.2,"unit":"g",
            "percentOfDailyNeeds":2.26},{"name":"Sugar","amount":6.69,"unit":"g","percentOfDailyNeeds":7.43},
            {"name":"Cholesterol","amount":31.0,"unit":"mg","percentOfDailyNeeds":10.33},{"name":"Sodium",
            "amount":67.19,"unit":"mg","percentOfDailyNeeds":2.92},{"name":"Protein","amount":10.93,"unit":"g",
            "percentOfDailyNeeds":21.87},{"name":"Calcium","amount":315.63,"unit":"mg","percentOfDailyNeeds":31.56},
            {"name":"Phosphorus","amount":239.89,"unit":"mg","percentOfDailyNeeds":23.99},{"name":"Manganese",
            "amount":0.41,"unit":"mg","percentOfDailyNeeds":20.7},{"name":"Fiber","amount":5.17,"unit":"g",
            "percentOfDailyNeeds":20.7},{"name":"Vitamin B12","amount":1.01,"unit":"µg","percentOfDailyNeeds":16.78},
            {"name":"Selenium","amount":10.49,"unit":"µg","percentOfDailyNeeds":14.99},{"name":"Vitamin A",
            "amount":730.96,"unit":"IU","percentOfDailyNeeds":14.62},{"name":"Potassium","amount":490.53,"unit":"mg",
            "percentOfDailyNeeds":14.02},{"name":"Vitamin C","amount":10.14,"unit":"mg","percentOfDailyNeeds":12.29},
            {"name":"Zinc","amount":1.79,"unit":"mg","percentOfDailyNeeds":11.91},{"name":"Folate","amount":44.09,
            "unit":"µg","percentOfDailyNeeds":11.02},{"name":"Vitamin K","amount":10.39,"unit":"µg",
            "percentOfDailyNeeds":9.9},{"name":"Vitamin B2","amount":0.17,"unit":"mg","percentOfDailyNeeds":9.82},
            {"name":"Vitamin B6","amount":0.19,"unit":"mg","percentOfDailyNeeds":9.56},{"name":"Magnesium",
            "amount":37.9,"unit":"mg","percentOfDailyNeeds":9.47},{"name":"Copper","amount":0.17,"unit":"mg",
            "percentOfDailyNeeds":8.45},{"name":"Vitamin B3","amount":1.31,"unit":"mg","percentOfDailyNeeds":6.52},
            {"name":"Vitamin E","amount":0.93,"unit":"mg","percentOfDailyNeeds":6.17},{"name":"Vitamin B5",
            "amount":0.62,"unit":"mg","percentOfDailyNeeds":6.16},{"name":"Vitamin B1","amount":0.08,"unit":"mg",
            "percentOfDailyNeeds":5.43},{"name":"Iron","amount":0.53,"unit":"mg","percentOfDailyNeeds":2.96}],
            "properties":[{"name":"Glycemic Index","amount":55.0,"unit":""},{"name":"Glycemic Load","amount":1.95,
            "unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,"unit":"mg"},{"name":"Petunidin","amount":0.0,
            "unit":"mg"},{"name":"Delphinidin","amount":130.82,"unit":"mg"},{"name":"Malvidin","amount":0.0,
            "unit":"mg"},{"name":"Pelargonidin","amount":0.0,"unit":"mg"},{"name":"Peonidin","amount":0.0,
            "unit":"mg"},{"name":"Catechin","amount":0.0,"unit":"mg"},{"name":"Epigallocatechin","amount":0.0,
            "unit":"mg"},{"name":"Epicatechin","amount":0.0,"unit":"mg"},{"name":"Epicatechin 3-gallate",
            "amount":0.0,"unit":"mg"},{"name":"Epigallocatechin 3-gallate","amount":0.0,"unit":"mg"},
            {"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins","amount":0.0,"unit":""},
            {"name":"Eriodictyol","amount":0.0,"unit":""},{"name":"Hesperetin","amount":0.0,"unit":"mg"},
            {"name":"Naringenin","amount":0.34,"unit":"mg"},{"name":"Apigenin","amount":0.0,"unit":"mg"},
            {"name":"Luteolin","amount":0.0,"unit":"mg"},{"name":"Isorhamnetin","amount":0.0,"unit":"mg"},
            {"name":"Kaempferol","amount":0.04,"unit":"mg"},{"name":"Myricetin","amount":0.06,"unit":"mg"},
            {"name":"Quercetin","amount":0.35,"unit":"mg"},{"name":"Theaflavin-3,3'-digallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate",
            "amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,"unit":"mg"}],"ingredients":[{"id":11209,
            "name":"eggplant","amount":0.33,"unit":"large","nutrients":[{"name":"Vitamin B3","amount":0.99,
            "unit":"mg"},{"name":"Folate","amount":33.59,"unit":"µg"},{"name":"Sugar","amount":5.39,"unit":"g"},
            {"name":"Magnesium","amount":21.37,"unit":"mg"},{"name":"Zinc","amount":0.24,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.12,"unit":"g"},{"name":"Vitamin B6","amount":0.13,"unit":"mg"},
            {"name":"Vitamin E","amount":0.46,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.06,"unit":"mg"},{"name":"Vitamin A","amount":35.11,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.02,"unit":"g"},{"name":"Manganese","amount":0.35,"unit":"mg"},
            {"name":"Vitamin C","amount":3.36,"unit":"mg"},{"name":"Selenium","amount":0.46,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":4.4,"unit":"g"},{"name":"Vitamin B5","amount":0.43,"unit":"mg"},{"name":"Vitamin 
            K","amount":5.34,"unit":"µg"},{"name":"Saturated Fat","amount":0.05,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.06,"unit":"mg"},{"name":"Fiber","amount":4.58,
            "unit":"g"},{"name":"Iron","amount":0.35,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":36.64,"unit":"mg"},{"name":"Carbohydrates","amount":8.98,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":3.05,"unit":"mg"},
            {"name":"Calcium","amount":13.74,"unit":"mg"},{"name":"Potassium","amount":349.61,"unit":"mg"},
            {"name":"Choline","amount":10.53,"unit":"mg"},{"name":"Calories","amount":38.17,"unit":"kcal"},
            {"name":"Copper","amount":0.12,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":1.5,"unit":"g"},{"name":"Fat","amount":0.27,"unit":"g"}]},{"id":11529,
            "name":"tomatoes","amount":3.33,"unit":"Tbs","nutrients":[{"name":"Vitamin B3","amount":0.29,
            "unit":"mg"},{"name":"Folate","amount":7.39,"unit":"µg"},{"name":"Sugar","amount":1.3,"unit":"g"},
            {"name":"Magnesium","amount":5.42,"unit":"mg"},{"name":"Zinc","amount":0.08,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.04,"unit":"g"},{"name":"Vitamin B6","amount":0.04,"unit":"mg"},
            {"name":"Vitamin E","amount":0.27,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.02,"unit":"mg"},{"name":"Vitamin A","amount":410.39,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.02,"unit":"g"},{"name":"Fluoride","amount":1.13,"unit":"mg"},
            {"name":"Manganese","amount":0.06,"unit":"mg"},{"name":"Vitamin C","amount":6.75,"unit":"mg"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":1.33,"unit":"g"},
            {"name":"Vitamin B5","amount":0.04,"unit":"mg"},{"name":"Vitamin K","amount":3.89,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.01,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.59,"unit":"g"},{"name":"Iron",
            "amount":0.13,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":11.82,"unit":"mg"},{"name":"Carbohydrates","amount":1.92,"unit":"g"},{"name":"Lycopene",
            "amount":1266.15,"unit":"µg"},{"name":"Sodium","amount":2.46,"unit":"mg"},{"name":"Calcium",
            "amount":4.93,"unit":"mg"},{"name":"Potassium","amount":116.76,"unit":"mg"},{"name":"Choline",
            "amount":3.3,"unit":"mg"},{"name":"Calories","amount":8.87,"unit":"kcal"},{"name":"Copper","amount":0.03,
            "unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.43,"unit":"g"},
            {"name":"Fat","amount":0.1,"unit":"g"}]},{"id":1040,"name":"swiss cheese","amount":33.33,"unit":"g",
            "nutrients":[{"name":"Vitamin B3","amount":0.02,"unit":"mg"},{"name":"Folate","amount":3.0,"unit":"µg"},
            {"name":"Sugar","amount":0.0,"unit":"g"},{"name":"Magnesium","amount":11.0,"unit":"mg"},{"name":"Zinc",
            "amount":1.46,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.38,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.02,"unit":"mg"},{"name":"Vitamin E","amount":0.2,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A",
            "amount":276.67,"unit":"IU"},{"name":"Vitamin B12","amount":1.01,"unit":"µg"},{"name":"Cholesterol",
            "amount":31.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":2.42,"unit":"g"},{"name":"Manganese",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":10.03,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.48,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.14,"unit":"mg"},{"name":"Vitamin K","amount":0.47,"unit":"µg"},{"name":"Saturated Fat",
            "amount":6.07,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.1,
            "unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":0.04,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":191.33,"unit":"mg"},
            {"name":"Carbohydrates","amount":0.48,"unit":"g"},{"name":"Lycopene","amount":0.33,"unit":"µg"},
            {"name":"Sodium","amount":61.67,"unit":"mg"},{"name":"Calcium","amount":296.67,"unit":"mg"},
            {"name":"Potassium","amount":23.67,"unit":"mg"},{"name":"Choline","amount":4.6,"unit":"mg"},
            {"name":"Calories","amount":131.0,"unit":"kcal"},{"name":"Copper","amount":0.02,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":9.0,"unit":"g"},{"name":"Fat",
            "amount":10.33,"unit":"g"}]},{"id":2044,"name":"basil leaves","amount":0.33,"unit":"leaves","nutrients":[
            {"name":"Vitamin B3","amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.11,"unit":"µg"},
            {"name":"Sugar","amount":0.0,"unit":"g"},{"name":"Magnesium","amount":0.11,"unit":"mg"},{"name":"Zinc",
            "amount":0.0,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,
            "unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":8.79,
            "unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,
            "unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Vitamin C","amount":0.03,"unit":"mg"},{"name":"Selenium","amount":0.0,"unit":"µg"},
            {"name":"Net Carbohydrates","amount":0.0,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},
            {"name":"Vitamin K","amount":0.69,"unit":"µg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},
            {"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},
            {"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":0.01,"unit":"mg"},{"name":"Caffeine",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.09,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.01,
            "unit":"mg"},{"name":"Calcium","amount":0.3,"unit":"mg"},{"name":"Potassium","amount":0.49,"unit":"mg"},
            {"name":"Choline","amount":0.02,"unit":"mg"},{"name":"Calories","amount":0.04,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.01,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":23.56,"percentFat":51.92,"percentCarbs":24.52},"weightPerServing":{
            "amount":235,"unit":"g"}},"summary":"If you have around <b>around 45 minutes</b> to spend in the kitchen, 
            Eggplant pizzette might be a super <b>gluten free, lacto ovo vegetarian, and primal</b> recipe to try. 
            One serving contains <b>174 calories</b>, <b>11g of protein</b>, and <b>10g of fat</b>. For <b>$1.13 per 
            serving</b>, this recipe <b>covers 11%</b> of your daily requirements of vitamins and minerals. This 
            recipe serves 3. Head to the store and pick up round eggplant, basil and oregano leaves, swiss cheese, 
            and a few other things to make it today. It works well as a budget friendly side dish. 5 people were glad 
            they tried this recipe. It is brought to you by Foodista. Overall, this recipe earns a <b>good 
            spoonacular score of 69%</b>. Similar recipes are <a 
            href=\"https://spoonacular.com/recipes/margherita-pizzette-516272\">Margherita Pizzette</a>, 
            <a href=\"https://spoonacular.com/recipes/nicoise-salad-pizzette-338453\">Nicoise Salad Pizzette</a>, 
            and <a href=\"https://spoonacular.com/recipes/eat-seasonal-zucchini-pizzette-1019700\">Eat Seasonal: 
            Zucchini Pizzette</a>.","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","lacto ovo 
            vegetarian","primal"],"occasions":[],"analyzedInstructions":[{"name":"","steps":[{"number":1,
            "step":"Place eggplant rounds in a non-stick pan greased with olive oil and bake in the oven for 10 
            minutes at 230C.","ingredients":[{"id":4053,"name":"olive oil","localizedName":"olive oil",
            "image":"olive-oil.jpg"},{"id":11209,"name":"eggplant","localizedName":"eggplant",
            "image":"eggplant.png"}],"equipment":[{"id":404784,"name":"oven","localizedName":"oven",
            "image":"oven.jpg","temperature":{"number":230.0,"unit":"Celsius"}},{"id":404645,"name":"frying pan",
            "localizedName":"frying pan","image":"pan.png"}],"length":{"number":10,"unit":"minutes"}},{"number":2,
            "step":"Remove the pan from oven, but leave baked eggplant inside.","ingredients":[{"id":11209,
            "name":"eggplant","localizedName":"eggplant","image":"eggplant.png"}],"equipment":[{"id":404784,
            "name":"oven","localizedName":"oven","image":"oven.jpg"},{"id":404645,"name":"frying pan",
            "localizedName":"frying pan","image":"pan.png"}]},{"number":3,"step":"Cover each eggplant round with one 
            spoon of chopped tomatoes, sprinkle with oregano and basil leaves.","ingredients":[{"id":2044,
            "name":"fresh basil","localizedName":"fresh basil","image":"fresh-basil.jpg"},{"id":11209,
            "name":"eggplant","localizedName":"eggplant","image":"eggplant.png"},{"id":11529,"name":"tomato",
            "localizedName":"tomato","image":"tomato.png"},{"id":2027,"name":"oregano","localizedName":"oregano",
            "image":"oregano.jpg"}],"equipment":[]},{"number":4,"step":"Top with grated cheese and bake an additional 
            5 minutes in the oven at the same temperature, until cheese is melted and golden brown.","ingredients":[{
            "id":1041009,"name":"cheese","localizedName":"cheese","image":"cheddar-cheese.png"}],"equipment":[{
            "id":404784,"name":"oven","localizedName":"oven","image":"oven.jpg"}],"length":{"number":5,
            "unit":"minutes"}},{"number":5,"step":"Serve pizzette warm or cooled as an appetizer or as a stand-alone 
            small meal.","ingredients":[],"equipment":[]}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/eggplant-pizzette-642303","usedIngredientCount":1,
            "missedIngredientCount":3,"likes":0,"missedIngredients":[{"id":11209,"amount":1.0,"unit":"large",
            "unitLong":"large","unitShort":"large","aisle":"Produce","name":"eggplant","original":"1 large round 
            eggplant, washed, sliced into rounds","originalName":"round eggplant, washed, sliced into rounds",
            "meta":["washed","sliced into rounds"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/eggplant.png"},{"id":1040,"amount":100.0,
            "unit":"g","unitLong":"grams","unitShort":"g","aisle":"Cheese","name":"swiss cheese","original":"100g 
            Swiss cheese, coarsely grated","originalName":"Swiss cheese, coarsely grated","meta":["grated"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/Swiss-cheese.jpg"},{"id":2044,"amount":1.0,
            "unit":"leaves","unitLong":"leave","unitShort":"leaf","aisle":"Produce","name":"basil leaves",
            "original":"Basil and oregano leaves, fresh or dried","originalName":"Basil and oregano , 
            fresh or dried","meta":["fresh"],"extendedName":"fresh basil leaves",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/fresh-basil.jpg"}],"usedIngredients":[{
            "id":11529,"amount":10.0,"unit":"Tbs","unitLong":"Tbs","unitShort":"Tbs","aisle":"Produce",
            "name":"tomatoes","original":"10 Tbs chopped tomatoes","originalName":"chopped tomatoes",
            "meta":["chopped"],"image":"https://spoonacular.com/cdn/ingredients_100x100/tomato.png"}],
            "unusedIngredients":[]},{"vegetarian":false,"vegan":false,"glutenFree":false,"dairyFree":false,
            "veryHealthy":false,"cheap":false,"veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":3,
            "gaps":"no","lowFodmap":false,"aggregateLikes":7,"spoonacularScore":50.0,"healthScore":7.0,
            "creditsText":"Jen West","sourceName":"Pink When","pricePerServing":182.15,"extendedIngredients":[{
            "id":99037,"aisle":"Pasta and Rice","image":"no.jpg","consistency":"solid","name":"burger skillet",
            "nameClean":"hamburger helper","original":"small personal skillet","originalName":"personal skillet",
            "amount":1.0,"unit":"small","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"small",
            "unitLong":"small"},"metric":{"amount":1.0,"unitShort":"small","unitLong":"small"}}},{"id":10311529,
            "aisle":"Produce","image":"cherry-tomatoes.png","consistency":"solid","name":"cherry tomatoes",
            "nameClean":"cherry tomato","original":"cherry tomatoes, halved","originalName":"cherry tomatoes, 
            halved","amount":1.0,"unit":"serving","meta":["halved"],"measures":{"us":{"amount":1.0,
            "unitShort":"serving","unitLong":"serving"},"metric":{"amount":1.0,"unitShort":"serving",
            "unitLong":"serving"}}},{"id":1123,"aisle":"Milk, Eggs, Other Dairy","image":"egg.png",
            "consistency":"solid","name":"eggs","nameClean":"egg","original":"2-3 lightly beaten eggs",
            "originalName":"lightly beaten eggs","amount":2.0,"unit":"","meta":["lightly beaten"],"measures":{"us":{
            "amount":2.0,"unitShort":"","unitLong":""},"metric":{"amount":2.0,"unitShort":"","unitLong":""}}},
            {"id":10011457,"aisle":"Produce","image":"spinach.jpg","consistency":"solid","name":"spinach leaves",
            "nameClean":"spinach","original":"spinach leaves","originalName":"spinach","amount":1.0,"unit":"leaves",
            "meta":[],"measures":{"us":{"amount":1.0,"unitShort":"leaf","unitLong":"leave"},"metric":{"amount":1.0,
            "unitShort":"leaf","unitLong":"leave"}}}],"id":769775,"title":"Simple Spinach and Tomato Frittata",
            "readyInMinutes":45,"servings":1,"sourceUrl":"http://www.pinkwhen.com/spinach-and-tomato-frittata/",
            "image":"https://spoonacular.com/recipeImages/769775-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":156.15,"unit":"kcal","percentOfDailyNeeds":7.81},{"name":"Fat",
            "amount":8.55,"unit":"g","percentOfDailyNeeds":13.16},{"name":"Saturated Fat","amount":2.78,"unit":"g",
            "percentOfDailyNeeds":17.36},{"name":"Carbohydrates","amount":7.32,"unit":"g",
            "percentOfDailyNeeds":2.44},{"name":"Net Carbohydrates","amount":6.23,"unit":"g",
            "percentOfDailyNeeds":2.27},{"name":"Sugar","amount":4.08,"unit":"g","percentOfDailyNeeds":4.53},
            {"name":"Cholesterol","amount":327.36,"unit":"mg","percentOfDailyNeeds":109.12},{"name":"Sodium",
            "amount":167.34,"unit":"mg","percentOfDailyNeeds":7.28},{"name":"Protein","amount":12.62,"unit":"g",
            "percentOfDailyNeeds":25.23},{"name":"Vitamin C","amount":34.03,"unit":"mg","percentOfDailyNeeds":41.24},
            {"name":"Selenium","amount":27.77,"unit":"µg","percentOfDailyNeeds":39.67},{"name":"Vitamin B2",
            "amount":0.44,"unit":"mg","percentOfDailyNeeds":25.87},{"name":"Vitamin A","amount":1292.69,"unit":"IU",
            "percentOfDailyNeeds":25.85},{"name":"Phosphorus","amount":216.17,"unit":"mg",
            "percentOfDailyNeeds":21.62},{"name":"Folate","amount":62.54,"unit":"µg","percentOfDailyNeeds":15.63},
            {"name":"Vitamin B5","amount":1.54,"unit":"mg","percentOfDailyNeeds":15.41},{"name":"Iron","amount":2.6,
            "unit":"mg","percentOfDailyNeeds":14.42},{"name":"Vitamin B6","amount":0.27,"unit":"mg",
            "percentOfDailyNeeds":13.42},{"name":"Vitamin B12","amount":0.78,"unit":"µg",
            "percentOfDailyNeeds":13.05},{"name":"Potassium","amount":451.54,"unit":"mg","percentOfDailyNeeds":12.9},
            {"name":"Vitamin E","amount":1.77,"unit":"mg","percentOfDailyNeeds":11.82},{"name":"Vitamin D",
            "amount":1.76,"unit":"µg","percentOfDailyNeeds":11.73},{"name":"Manganese","amount":0.19,"unit":"mg",
            "percentOfDailyNeeds":9.45},{"name":"Zinc","amount":1.35,"unit":"mg","percentOfDailyNeeds":8.98},
            {"name":"Vitamin K","amount":9.24,"unit":"µg","percentOfDailyNeeds":8.8},{"name":"Copper","amount":0.18,
            "unit":"mg","percentOfDailyNeeds":8.78},{"name":"Calcium","amount":66.55,"unit":"mg",
            "percentOfDailyNeeds":6.66},{"name":"Vitamin B1","amount":0.1,"unit":"mg","percentOfDailyNeeds":6.42},
            {"name":"Magnesium","amount":24.67,"unit":"mg","percentOfDailyNeeds":6.17},{"name":"Vitamin B3",
            "amount":0.91,"unit":"mg","percentOfDailyNeeds":4.55},{"name":"Fiber","amount":1.09,"unit":"g",
            "percentOfDailyNeeds":4.36}],"properties":[{"name":"Glycemic Index","amount":32.0,"unit":""},
            {"name":"Glycemic Load","amount":0.0,"unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,
            "unit":"mg"},{"name":"Petunidin","amount":0.0,"unit":"mg"},{"name":"Delphinidin","amount":0.0,
            "unit":"mg"},{"name":"Malvidin","amount":0.0,"unit":"mg"},{"name":"Pelargonidin","amount":0.0,
            "unit":"mg"},{"name":"Peonidin","amount":0.0,"unit":"mg"},{"name":"Catechin","amount":0.0,"unit":"mg"},
            {"name":"Epigallocatechin","amount":0.0,"unit":"mg"},{"name":"Epicatechin","amount":0.0,"unit":"mg"},
            {"name":"Epicatechin 3-gallate","amount":0.0,"unit":"mg"},{"name":"Epigallocatechin 3-gallate",
            "amount":0.0,"unit":"mg"},{"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins",
            "amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},{"name":"Hesperetin","amount":0.0,
            "unit":"mg"},{"name":"Naringenin","amount":0.0,"unit":"mg"},{"name":"Apigenin","amount":0.0,"unit":"mg"},
            {"name":"Luteolin","amount":0.02,"unit":"mg"},{"name":"Isorhamnetin","amount":0.0,"unit":""},
            {"name":"Kaempferol","amount":0.08,"unit":"mg"},{"name":"Myricetin","amount":0.02,"unit":"mg"},
            {"name":"Quercetin","amount":1.08,"unit":"mg"},{"name":"Theaflavin-3,3'-digallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate",
            "amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,"unit":"mg"}],"ingredients":[{"id":99037,
            "name":"burger skillet","amount":1.0,"unit":"small","nutrients":[{"name":"Vitamin B3","amount":0.05,
            "unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.06,"unit":"g"},
            {"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.01,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,"unit":"mg"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Trans Fat","amount":0.02,"unit":"g"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.69,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.03,"unit":"g"},{"name":"Iron",
            "amount":0.02,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":0.0,"unit":"mg"},{"name":"Carbohydrates","amount":0.72,"unit":"g"},{"name":"Sodium",
            "amount":25.31,"unit":"mg"},{"name":"Calcium","amount":0.0,"unit":"mg"},{"name":"Potassium",
            "amount":1.88,"unit":"mg"},{"name":"Calories","amount":3.44,"unit":"kcal"},{"name":"Copper","amount":0.0,
            "unit":"mg"},{"name":"Protein","amount":0.09,"unit":"g"},{"name":"Fat","amount":0.02,"unit":"g"}]},
            {"id":10311529,"name":"cherry tomatoes","amount":1.0,"unit":"serving","nutrients":[{"name":"Vitamin B3",
            "amount":0.79,"unit":"mg"},{"name":"Folate","amount":19.24,"unit":"µg"},{"name":"Sugar","amount":3.69,
            "unit":"g"},{"name":"Magnesium","amount":13.32,"unit":"mg"},{"name":"Zinc","amount":0.21,"unit":"mg"},
            {"name":"Poly Unsaturated Fat","amount":0.07,"unit":"g"},{"name":"Vitamin B6","amount":0.12,"unit":"mg"},
            {"name":"Vitamin E","amount":0.83,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.05,"unit":"mg"},{"name":"Vitamin A","amount":723.72,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.02,"unit":"g"},{"name":"Manganese","amount":0.16,"unit":"mg"},
            {"name":"Vitamin C","amount":33.74,"unit":"mg"},{"name":"Selenium","amount":0.74,"unit":"µg"},
            {"name":"Net Carbohydrates","amount":4.9,"unit":"g"},{"name":"Vitamin B5","amount":0.19,"unit":"mg"},
            {"name":"Vitamin K","amount":4.14,"unit":"µg"},{"name":"Saturated Fat","amount":0.02,"unit":"g"},
            {"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.03,"unit":"mg"},
            {"name":"Fiber","amount":1.04,"unit":"g"},{"name":"Iron","amount":1.01,"unit":"mg"},{"name":"Caffeine",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":41.44,"unit":"mg"},{"name":"Carbohydrates",
            "amount":5.93,"unit":"g"},{"name":"Lycopene","amount":4500.68,"unit":"µg"},{"name":"Sodium",
            "amount":16.28,"unit":"mg"},{"name":"Calcium","amount":16.28,"unit":"mg"},{"name":"Potassium",
            "amount":322.64,"unit":"mg"},{"name":"Choline","amount":10.21,"unit":"mg"},{"name":"Calories",
            "amount":26.64,"unit":"kcal"},{"name":"Copper","amount":0.11,"unit":"mg"},{"name":"Folic Acid",
            "amount":0.0,"unit":"µg"},{"name":"Protein","amount":1.41,"unit":"g"},{"name":"Fat","amount":0.16,
            "unit":"g"}]},{"id":1123,"name":"eggs","amount":2.0,"unit":"","nutrients":[{"name":"Vitamin B3",
            "amount":0.07,"unit":"mg"},{"name":"Folate","amount":41.36,"unit":"µg"},{"name":"Sugar","amount":0.33,
            "unit":"g"},{"name":"Magnesium","amount":10.56,"unit":"mg"},{"name":"Zinc","amount":1.14,"unit":"mg"},
            {"name":"Poly Unsaturated Fat","amount":1.68,"unit":"g"},{"name":"Vitamin B6","amount":0.15,"unit":"mg"},
            {"name":"Vitamin E","amount":0.92,"unit":"mg"},{"name":"Vitamin D","amount":1.76,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.04,"unit":"mg"},{"name":"Vitamin A","amount":475.2,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.78,"unit":"µg"},{"name":"Cholesterol","amount":327.36,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":3.22,"unit":"g"},{"name":"Fluoride","amount":0.97,"unit":"mg"},
            {"name":"Manganese","amount":0.02,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},
            {"name":"Trans Fat","amount":0.03,"unit":"g"},{"name":"Selenium","amount":27.02,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":0.63,"unit":"g"},{"name":"Vitamin B5","amount":1.35,"unit":"mg"},{"name":"Vitamin 
            K","amount":0.26,"unit":"µg"},{"name":"Saturated Fat","amount":2.75,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.4,"unit":"mg"},{"name":"Fiber","amount":0.0,
            "unit":"g"},{"name":"Iron","amount":1.54,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":174.24,"unit":"mg"},{"name":"Carbohydrates","amount":0.63,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":124.96,"unit":"mg"},
            {"name":"Calcium","amount":49.28,"unit":"mg"},{"name":"Potassium","amount":121.44,"unit":"mg"},
            {"name":"Choline","amount":258.72,"unit":"mg"},{"name":"Calories","amount":125.84,"unit":"kcal"},
            {"name":"Copper","amount":0.06,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":11.09,"unit":"g"},{"name":"Fat","amount":8.37,"unit":"g"}]},{"id":10011457,
            "name":"spinach leaves","amount":1.0,"unit":"leaves","nutrients":[{"name":"Vitamin B3","amount":0.01,
            "unit":"mg"},{"name":"Folate","amount":1.94,"unit":"µg"},{"name":"Sugar","amount":0.0,"unit":"g"},
            {"name":"Magnesium","amount":0.79,"unit":"mg"},{"name":"Zinc","amount":0.01,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            E","amount":0.02,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":93.77,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.01,"unit":"mg"},{"name":"Vitamin C",
            "amount":0.28,"unit":"mg"},{"name":"Selenium","amount":0.01,"unit":"µg"},{"name":"Net Carbohydrates",
            "amount":0.01,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K",
            "amount":4.83,"unit":"µg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.02,
            "unit":"g"},{"name":"Iron","amount":0.03,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":0.49,"unit":"mg"},{"name":"Carbohydrates","amount":0.04,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.79,"unit":"mg"},
            {"name":"Calcium","amount":0.99,"unit":"mg"},{"name":"Potassium","amount":5.58,"unit":"mg"},
            {"name":"Choline","amount":0.19,"unit":"mg"},{"name":"Calories","amount":0.23,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.03,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":32.2,"percentFat":49.11,"percentCarbs":18.69},"weightPerServing":{
            "amount":238,"unit":"g"}},"summary":"Simple Spinach and Tomato Frittata might be just the main course you 
            are searching for. For <b>$1.82 per serving</b>, this recipe <b>covers 14%</b> of your daily requirements 
            of vitamins and minerals. This recipe makes 1 servings with <b>156 calories</b>, <b>13g of protein</b>, 
            and <b>9g of fat</b> each. Not a lot of people made this recipe, and 7 would say it hit the spot. If you 
            have personal skillet, cherry tomatoes, spinach leaves, and a few other ingredients on hand, you can make 
            it. All things considered, we decided this recipe <b>deserves a spoonacular score of 52%</b>. This score 
            is good. Try <a href=\"https://spoonacular.com/recipes/simple-spinach-ricotta-frittata-19504\">Simple 
            Spinach & Ricotta Frittata</a>, 
            <a href=\"https://spoonacular.com/recipes/spinach-and-tomato-frittata-169326\">Spinach and Tomato 
            Frittata</a>, and <a href=\"https://spoonacular.com/recipes/ricotta-tomato-spinach-frittata-215063
            \">Ricotta, tomato & spinach frittata</a> for similar recipes.","cuisines":[],"dishTypes":["side dish"],
            "diets":[],"occasions":[],"analyzedInstructions":[],
            "spoonacularSourceUrl":"https://spoonacular.com/simple-spinach-and-tomato-frittata-769775",
            "usedIngredientCount":1,"missedIngredientCount":3,"likes":0,"missedIngredients":[{"id":99037,
            "amount":1.0,"unit":"small","unitLong":"small","unitShort":"small","aisle":"Pasta and Rice",
            "name":"burger skillet","original":"small personal skillet","originalName":"personal skillet","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/no.jpg"},{"id":1123,"amount":2.0,"unit":"",
            "unitLong":"","unitShort":"","aisle":"Milk, Eggs, Other Dairy","name":"eggs","original":"2-3 lightly 
            beaten eggs","originalName":"lightly beaten eggs","meta":["lightly beaten"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/egg.png"},{"id":10011457,"amount":1.0,
            "unit":"leaves","unitLong":"leave","unitShort":"leaf","aisle":"Produce","name":"spinach leaves",
            "original":"spinach leaves","originalName":"spinach","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/spinach.jpg"}],"usedIngredients":[{
            "id":10311529,"amount":1.0,"unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Produce",
            "name":"cherry tomatoes","original":"cherry tomatoes, halved","originalName":"cherry tomatoes, halved",
            "meta":["halved"],"image":"https://spoonacular.com/cdn/ingredients_100x100/cherry-tomatoes.png"}],
            "unusedIngredients":[]}],"offset":0,"number":5,"totalResults":726}'''),
            StringWithAttributeText(r'''{"results":[{"vegetarian":true,"vegan":true,"glutenFree":true,
            "dairyFree":true,"veryHealthy":false,"cheap":false,"veryPopular":false,"sustainable":false,
            "weightWatcherSmartPoints":0,"gaps":"no","lowFodmap":true,"aggregateLikes":0,"spoonacularScore":2.0,
            "healthScore":2.0,"creditsText":"maplewoodroad","sourceName":"Maplewood Road","pricePerServing":6.89,
            "extendedIngredients":[{"id":12098,"aisle":"Produce","image":"chestnuts.jpg","consistency":"solid",
            "name":"all the nuts","nameClean":"chestnuts","original":"Of all the nuts, chestnuts are the only ones 
            that contain vitamin C.","originalName":"Of all the nuts, chestnuts are the only ones that contain 
            vitamin C","amount":1.0,"unit":"serving","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"serving",
            "unitLong":"serving"},"metric":{"amount":1.0,"unitShort":"serving","unitLong":"serving"}}},{"id":12098,
            "aisle":"Produce","image":"chestnuts.jpg","consistency":"solid","name":"roasted chestnuts were sold on 
            the streets of rome in the sixteenth century and are still sold on th","nameClean":"chestnuts",
            "original":"Roasted chestnuts were sold on the streets of Rome in the sixteenth century and are still 
            sold on the streets of European towns in the winter.","originalName":"Roasted chestnuts were sold on the 
            streets of Rome in the sixteenth century and are still sold on the streets of European towns in the 
            winter","amount":1.0,"unit":"serving","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"serving",
            "unitLong":"serving"},"metric":{"amount":1.0,"unitShort":"serving","unitLong":"serving"}}},{"id":12098,
            "aisle":"Produce","image":"chestnuts.jpg","consistency":"solid","name":"roman soldiers were given 
            chestnut porridge before entering battle","nameClean":"chestnuts","original":"Roman soldiers were given 
            chestnut porridge before entering battle.","originalName":"Roman soldiers were given chestnut porridge 
            before entering battle","amount":1.0,"unit":"serving","meta":[],"measures":{"us":{"amount":1.0,
            "unitShort":"serving","unitLong":"serving"},"metric":{"amount":1.0,"unitShort":"serving",
            "unitLong":"serving"}}},{"id":20444,"aisle":"Pasta and Rice","image":"uncooked-white-rice.png",
            "consistency":"solid","name":"chestnut is japan's most ancient fruit. kuri was cultivated even before 
            growing rice","nameClean":"rice","original":"Chestnut (Kuri in Japanese) is Japan's most ancient fruit. 
            Kuri was cultivated even before growing rice.","originalName":"Chestnut (Kuri in Japanese) is Japan's 
            most ancient fruit. Kuri was cultivated even before growing rice","amount":1.0,"unit":"serving",
            "meta":["(Kuri in Japanese)"],"measures":{"us":{"amount":1.0,"unitShort":"serving","unitLong":"serving"},
            "metric":{"amount":1.0,"unitShort":"serving","unitLong":"serving"}}},{"id":1002028,"aisle":"Spices and 
            Seasonings","image":"paprika.jpg","consistency":"solid","name":"in hungarian cuisine","nameClean":"sweet 
            paprika","original":"In Hungarian cuisine, cooked chestnuts are puréed, mixed with sugar (and usually 
            rum), forced through a ricer, and topped with whipped cream to make a dessert called gesztenyepüré – 
            chestnut purée.","originalName":"In Hungarian cuisine, cooked chestnuts are puréed, mixed with sugar (and 
            usually rum), forced through a ricer, and topped with whipped cream to make a dessert called 
            gesztenyepüré – chestnut purée","amount":1.0,"unit":"serving","meta":["mixed","with sugar (and usually 
            rum), forced through a ricer, and topped with whipped cream to make a dessert called gesztenyepüré - 
            chestnut purée.","cooked"],"measures":{"us":{"amount":1.0,"unitShort":"serving","unitLong":"serving"},
            "metric":{"amount":1.0,"unitShort":"serving","unitLong":"serving"}}},{"id":null,"aisle":"?","image":null,
            "consistency":null,"name":"in george orwell's 1984","nameClean":null,"original":"In George Orwell’s 1984, 
            the chestnut tree is used in poems recited throughout, referring to nature, modern life, and lies, 
            as in the saying: 'that old chestnut'.","originalName":"In George Orwell's 1984, the chestnut tree is 
            used in poems recited throughout, referring to nature, modern life, and lies, as in the saying: 'that old 
            chestnut'","amount":1.0,"unit":"serving","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"serving",
            "unitLong":"serving"},"metric":{"amount":1.0,"unitShort":"serving","unitLong":"serving"}}}],"id":1697797,
            "title":"Chestnuts Roasting on an Open Fire","author":"maplewoodroad","readyInMinutes":45,"servings":1,
            "sourceUrl":"https://maplewoodroad.com/chestnuts-roasting-on-an-open-fire/",
            "image":"https://spoonacular.com/recipeImages/1697797-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":12.35,"unit":"kcal","percentOfDailyNeeds":0.62},{"name":"Fat",
            "amount":0.17,"unit":"g","percentOfDailyNeeds":0.27},{"name":"Saturated Fat","amount":0.03,"unit":"g",
            "percentOfDailyNeeds":0.19},{"name":"Carbohydrates","amount":2.66,"unit":"g","percentOfDailyNeeds":0.89},
            {"name":"Net Carbohydrates","amount":2.3,"unit":"g","percentOfDailyNeeds":0.84},{"name":"Sugar",
            "amount":0.1,"unit":"g","percentOfDailyNeeds":0.12},{"name":"Cholesterol","amount":0.0,"unit":"mg",
            "percentOfDailyNeeds":0.0},{"name":"Sodium","amount":0.79,"unit":"mg","percentOfDailyNeeds":0.03},
            {"name":"Protein","amount":0.26,"unit":"g","percentOfDailyNeeds":0.52},{"name":"Vitamin A",
            "amount":493.32,"unit":"IU","percentOfDailyNeeds":9.87},{"name":"Vitamin E","amount":0.29,"unit":"mg",
            "percentOfDailyNeeds":1.95},{"name":"Manganese","amount":0.04,"unit":"mg","percentOfDailyNeeds":1.84},
            {"name":"Vitamin B6","amount":0.03,"unit":"mg","percentOfDailyNeeds":1.68},{"name":"Vitamin C",
            "amount":1.22,"unit":"mg","percentOfDailyNeeds":1.47},{"name":"Fiber","amount":0.36,"unit":"g",
            "percentOfDailyNeeds":1.45},{"name":"Iron","amount":0.25,"unit":"mg","percentOfDailyNeeds":1.38},
            {"name":"Potassium","amount":38.47,"unit":"mg","percentOfDailyNeeds":1.1},{"name":"Copper","amount":0.02,
            "unit":"mg","percentOfDailyNeeds":1.09}],"properties":[{"name":"Glycemic Index","amount":238.19,
            "unit":""},{"name":"Glycemic Load","amount":1.23,"unit":""}],"flavonoids":[{"name":"Cyanidin",
            "amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,"unit":""},{"name":"Delphinidin","amount":0.0,
            "unit":""},{"name":"Malvidin","amount":0.0,"unit":""},{"name":"Pelargonidin","amount":0.0,"unit":""},
            {"name":"Peonidin","amount":0.0,"unit":""},{"name":"Catechin","amount":0.0,"unit":"mg"},
            {"name":"Epigallocatechin","amount":0.0,"unit":"mg"},{"name":"Epicatechin","amount":0.0,"unit":"mg"},
            {"name":"Epicatechin 3-gallate","amount":0.0,"unit":"mg"},{"name":"Epigallocatechin 3-gallate",
            "amount":0.0,"unit":"mg"},{"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins",
            "amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},{"name":"Hesperetin","amount":0.0,
            "unit":""},{"name":"Naringenin","amount":0.0,"unit":""},{"name":"Apigenin","amount":0.0,"unit":""},
            {"name":"Luteolin","amount":0.0,"unit":""},{"name":"Isorhamnetin","amount":0.0,"unit":""},
            {"name":"Kaempferol","amount":0.0,"unit":""},{"name":"Myricetin","amount":0.0,"unit":""},
            {"name":"Quercetin","amount":0.0,"unit":""},{"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},
            {"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,
            "unit":""},{"name":"Gallocatechin","amount":0.0,"unit":"mg"}],"ingredients":[{"id":12098,"name":"all the 
            nuts","amount":1.0,"unit":"serving","nutrients":[{"name":"Vitamin B3","amount":0.01,"unit":"mg"},
            {"name":"Folate","amount":0.58,"unit":"µg"},{"name":"Magnesium","amount":0.3,"unit":"mg"},{"name":"Zinc",
            "amount":0.0,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.26,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.4,
            "unit":"mg"},{"name":"Net Carbohydrates","amount":0.44,"unit":"g"},{"name":"Vitamin B5","amount":0.0,
            "unit":"mg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,
            "unit":"mg"},{"name":"Iron","amount":0.01,"unit":"mg"},{"name":"Phosphorus","amount":0.38,"unit":"mg"},
            {"name":"Carbohydrates","amount":0.44,"unit":"g"},{"name":"Sodium","amount":0.02,"unit":"mg"},
            {"name":"Calcium","amount":0.19,"unit":"mg"},{"name":"Potassium","amount":4.84,"unit":"mg"},
            {"name":"Calories","amount":1.96,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.02,"unit":"g"},{"name":"Fat","amount":0.01,
            "unit":"g"}]},{"id":12098,"name":"roasted chestnuts were sold on the streets of rome in the sixteenth 
            century and are still sold on th","amount":1.0,"unit":"serving","nutrients":[{"name":"Vitamin B3",
            "amount":0.01,"unit":"mg"},{"name":"Folate","amount":0.58,"unit":"µg"},{"name":"Magnesium","amount":0.3,
            "unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,
            "unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.26,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.0,"unit":"mg"},
            {"name":"Vitamin C","amount":0.4,"unit":"mg"},{"name":"Net Carbohydrates","amount":0.44,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Iron","amount":0.01,"unit":"mg"},
            {"name":"Phosphorus","amount":0.38,"unit":"mg"},{"name":"Carbohydrates","amount":0.44,"unit":"g"},
            {"name":"Sodium","amount":0.02,"unit":"mg"},{"name":"Calcium","amount":0.19,"unit":"mg"},
            {"name":"Potassium","amount":4.84,"unit":"mg"},{"name":"Calories","amount":1.96,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.02,"unit":"g"},{"name":"Fat","amount":0.01,"unit":"g"}]},{"id":12098,
            "name":"roman soldiers were given chestnut porridge before entering battle","amount":1.0,
            "unit":"serving","nutrients":[{"name":"Vitamin B3","amount":0.01,"unit":"mg"},{"name":"Folate",
            "amount":0.58,"unit":"µg"},{"name":"Magnesium","amount":0.3,"unit":"mg"},{"name":"Zinc","amount":0.0,
            "unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,
            "unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,
            "unit":"mg"},{"name":"Vitamin A","amount":0.26,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,
            "unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,
            "unit":"g"},{"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.4,"unit":"mg"},
            {"name":"Net Carbohydrates","amount":0.44,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},
            {"name":"Iron","amount":0.01,"unit":"mg"},{"name":"Phosphorus","amount":0.38,"unit":"mg"},
            {"name":"Carbohydrates","amount":0.44,"unit":"g"},{"name":"Sodium","amount":0.02,"unit":"mg"},
            {"name":"Calcium","amount":0.19,"unit":"mg"},{"name":"Potassium","amount":4.84,"unit":"mg"},
            {"name":"Calories","amount":1.96,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.02,"unit":"g"},{"name":"Fat","amount":0.01,
            "unit":"g"}]},{"id":20444,"name":"chestnut is japan's most ancient fruit. kuri was cultivated even before 
            growing rice","amount":1.0,"unit":"serving","nutrients":[{"name":"Vitamin B3","amount":0.02,"unit":"mg"},
            {"name":"Folate","amount":0.08,"unit":"µg"},{"name":"Sugar","amount":0.0,"unit":"g"},{"name":"Magnesium",
            "amount":0.25,"unit":"mg"},{"name":"Zinc","amount":0.01,"unit":"mg"},{"name":"Poly Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin E","amount":0.0,
            "unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,
            "unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,
            "unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,
            "unit":"g"},{"name":"Manganese","amount":0.01,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},
            {"name":"Selenium","amount":0.15,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.79,"unit":"g"},
            {"name":"Vitamin B5","amount":0.01,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.01,"unit":"g"},{"name":"Iron",
            "amount":0.01,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":1.15,"unit":"mg"},{"name":"Carbohydrates","amount":0.8,"unit":"g"},{"name":"Lycopene",
            "amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.05,"unit":"mg"},{"name":"Calcium","amount":0.28,
            "unit":"mg"},{"name":"Potassium","amount":1.15,"unit":"mg"},{"name":"Choline","amount":0.06,"unit":"mg"},
            {"name":"Calories","amount":3.65,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.07,"unit":"g"},{"name":"Fat","amount":0.01,
            "unit":"g"}]},{"id":1002028,"name":"in hungarian cuisine","amount":1.0,"unit":"serving","nutrients":[{
            "name":"Vitamin B3","amount":0.1,"unit":"mg"},{"name":"Folate","amount":0.49,"unit":"µg"},
            {"name":"Sugar","amount":0.1,"unit":"g"},{"name":"Magnesium","amount":1.78,"unit":"mg"},{"name":"Zinc",
            "amount":0.04,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.08,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.02,"unit":"mg"},{"name":"Vitamin E","amount":0.29,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A",
            "amount":492.54,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.02,"unit":"g"},{"name":"Manganese",
            "amount":0.02,"unit":"mg"},{"name":"Vitamin C","amount":0.01,"unit":"mg"},{"name":"Trans Fat",
            "amount":0.0,"unit":"g"},{"name":"Selenium","amount":0.06,"unit":"µg"},{"name":"Net Carbohydrates",
            "amount":0.19,"unit":"g"},{"name":"Vitamin B5","amount":0.03,"unit":"mg"},{"name":"Vitamin K",
            "amount":0.8,"unit":"µg"},{"name":"Saturated Fat","amount":0.02,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.35,
            "unit":"g"},{"name":"Iron","amount":0.21,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":3.14,"unit":"mg"},{"name":"Carbohydrates","amount":0.54,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.68,"unit":"mg"},
            {"name":"Calcium","amount":2.29,"unit":"mg"},{"name":"Potassium","amount":22.8,"unit":"mg"},
            {"name":"Choline","amount":0.52,"unit":"mg"},{"name":"Calories","amount":2.82,"unit":"kcal"},
            {"name":"Copper","amount":0.01,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.14,"unit":"g"},{"name":"Fat","amount":0.13,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":7.89,"percentFat":11.74,"percentCarbs":80.37},"weightPerServing":{
            "amount":5,"unit":"g"}},"summary":"You can never have too many side dish recipes, so give Chestnuts 
            Roasting on an Open Fire a try. For <b>7 cents per serving</b>, this recipe <b>covers 1%</b> of your 
            daily requirements of vitamins and minerals. This recipe makes 1 servings with <b>16 calories</b>, 
            <b>0g of protein</b>, and <b>0g of fat</b> each. A mixture of in hungarian cuisine, chestnut is japan's 
            most ancient fruit. kuri was cultivated even before growing rice, in george orwell's 1984, and a handful 
            of other ingredients are all it takes to make this recipe so flavorful. From preparation to the plate, 
            this recipe takes around <b>around 45 minutes</b>. It is brought to you by spoonacular user <a 
            href=\"/profile/maplewoodroad\">maplewoodroad</a>. It is a good option if you're following a <b>gluten 
            free, dairy free, lacto ovo vegetarian, and fodmap friendly</b> diet. Users who liked this recipe also 
            liked <a href=\"https://spoonacular.com/recipes/cooking-over-an-open-fire-english-bacon-leek-and-potato
            -soup-251376\">Cooking Over an Open Fire: English Bacon, Leek and Potato Soup</a>, 
            <a href=\"https://spoonacular.com/recipes/brined-roasting-chicken-464140\">Brined Roasting Chicken</a>, 
            and <a href=\"https://spoonacular.com/recipes/oregano-roasting-chicken-450202\">Oregano Roasting 
            Chicken</a>.","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free","dairy free","lacto ovo 
            vegetarian","fodmap friendly","vegan"],"occasions":[],"analyzedInstructions":[{"name":"",
            "steps":[{"number":1,"step":"Preheat oven to 425℉","ingredients":[],"equipment":[{"id":404784,
            "name":"oven","localizedName":"oven","image":"oven.jpg"}]},{"number":2,"step":"Arrange the prepared 
            chestnuts evenly on a baking sheet","ingredients":[{"id":12098,"name":"chestnuts",
            "localizedName":"chestnuts","image":"chestnuts.jpg"}],"equipment":[{"id":404727,"name":"baking sheet",
            "localizedName":"baking sheet","image":"baking-sheet.jpg"}]},{"number":3,"step":"Roast for about 15 to 20 
            minutes or until the meat of the chestnut is soft ","ingredients":[{"id":12098,"name":"chestnuts",
            "localizedName":"chestnuts","image":"chestnuts.jpg"},{"id":1065062,"name":"meat","localizedName":"meat",
            "image":"whole-chicken.jpg"}],"equipment":[],"length":{"number":15,"unit":"minutes"}},{"number":4,
            "step":"Peel and eat (or peel, dip in melted butter, and eat)","ingredients":[{"id":1001,"name":"butter",
            "localizedName":"butter","image":"butter-sliced.jpg"},{"id":0,"name":"dip","localizedName":"dip",
            "image":""}],"equipment":[]}]},{"name":"And here’s the soundtrack to listen to while roasting your nuts",
            "steps":[{"number":1,"step":"Fun Facts About Chestnuts ","ingredients":[{"id":12098,"name":"chestnuts",
            "localizedName":"chestnuts","image":"chestnuts.jpg"}],"equipment":[]},{"number":2,"step":"Of all the 
            nuts, chestnuts are the only ones that contain vitamin C.","ingredients":[{"id":12098,"name":"chestnuts",
            "localizedName":"chestnuts","image":"chestnuts.jpg"},{"id":12135,"name":"nuts","localizedName":"nuts",
            "image":"nuts-mixed.jpg"}],"equipment":[]},{"number":3,"step":"Chestnut is of the same family of the oak, 
            and likewise its wood contains many tannins. This makes its wood very lasting, gives it excellent natural 
            outdoor resistance, and avoids the need for extra protection.","ingredients":[{"id":12098,
            "name":"chestnuts","localizedName":"chestnuts","image":"chestnuts.jpg"}],"equipment":[]},{"number":4,
            "step":"Roasted chestnuts were sold on the streets of Rome in the sixteenth century and are still sold on 
            the streets of European towns in the winter.","ingredients":[{"id":0,"name":"roasted chestnuts",
            "localizedName":"roasted chestnuts","image":"chestnuts.jpg"}],"equipment":[]},{"number":5,"step":"Roman 
            soldiers were given chestnut porridge before entering battle.","ingredients":[{"id":12098,
            "name":"chestnuts","localizedName":"chestnuts","image":"chestnuts.jpg"},{"id":0,"name":"hot cereal",
            "localizedName":"hot cereal","image":""}],"equipment":[]},{"number":6,"step":"Chestnut (Kuri in Japanese) 
            is Japan's most ancient fruit. Kuri was cultivated even before growing rice.","ingredients":[{"id":12098,
            "name":"chestnuts","localizedName":"chestnuts","image":"chestnuts.jpg"},{"id":9431,"name":"fruit",
            "localizedName":"fruit","image":"mixed-fresh-fruit.jpg"},{"id":10511643,"name":"red kuri squash",
            "localizedName":"red kuri squash","image":"kuri-or-hokkaido.jpg"},{"id":20444,"name":"rice",
            "localizedName":"rice","image":"uncooked-white-rice.png"}],"equipment":[]},{"number":7,"step":"In George 
            Orwell’s 1984, the chestnut tree is used in poems recited throughout, referring to nature, modern life, 
            and lies, as in the saying: 'that old chestnut'.","ingredients":[{"id":12098,"name":"chestnuts",
            "localizedName":"chestnuts","image":"chestnuts.jpg"}],"equipment":[]},{"number":8,"step":"In Hungarian cuisine, cooked chestnuts are puréed, mixed with sugar (and usually rum), forced through a ricer, 
            and topped with whipped cream to make a dessert called gesztenyepüré – chestnut purée.","ingredients":[{
            "id":1054,"name":"whipped cream","localizedName":"whipped cream","image":"whipped-cream.jpg"},
            {"id":12098,"name":"chestnuts","localizedName":"chestnuts","image":"chestnuts.jpg"},{"id":19335,
            "name":"sugar","localizedName":"sugar","image":"sugar-in-bowl.png"},{"id":11114037,"name":"rum",
            "localizedName":"rum","image":"rum-dark.jpg"}],"equipment":[{"id":404790,"name":"potato ricer",
            "localizedName":"potato ricer","image":"potato-ricer.jpg"}]},{"number":9,"step":"Chestnuts can be 
            consumed raw, baked, boiled, or roasted. They also can be dried and milled into flour, which can then be 
            used to prepare breads, cakes, pies, pancakes, pastas, polenta, or used as a thickener for stews, soups, 
            and sauces.","ingredients":[{"id":12098,"name":"chestnuts","localizedName":"chestnuts",
            "image":"chestnuts.jpg"},{"id":10035137,"name":"polenta","localizedName":"polenta",
            "image":"cornmeal.png"},{"id":20081,"name":"all purpose flour","localizedName":"all purpose flour",
            "image":"flour.png"}],"equipment":[]},{"number":10,"step":"Just roasting some nuts","ingredients":[{
            "id":12135,"name":"nuts","localizedName":"nuts","image":"nuts-mixed.jpg"}],"equipment":[]},{"number":11,
            "step":"Did you make this Roasted Chestnuts recipe?","ingredients":[{"id":0,"name":"roasted chestnuts",
            "localizedName":"roasted chestnuts","image":"chestnuts.jpg"}],"equipment":[]},{"number":12,"step":"Let us 
            know in the comments below!","ingredients":[],"equipment":[]},{"number":13,"step":"Content and 
            photographs are copyright protected. Sharing of this recipe is both encouraged and appreciated. Copying 
            and/or pasting full recipes to any social media is strictly prohibited.","ingredients":[],"equipment":[
            ]}]}],"spoonacularSourceUrl":"https://spoonacular.com/chestnuts-roasting-on-an-open-fire-1697797",
            "usedIngredientCount":1,"missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":12098,
            "amount":1.0,"unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Produce","name":"all the nuts","original":"Of all the nuts, chestnuts are the only ones that contain vitamin C.",
            "originalName":"Of all the nuts, chestnuts are the only ones that contain vitamin C","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/chestnuts.jpg"},{"id":1002028,"amount":1.0,
            "unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Spices and Seasonings","name":"in hungarian cuisine","original":"In Hungarian cuisine, cooked chestnuts are puréed, mixed with sugar (and 
            usually rum), forced through a ricer, and topped with whipped cream to make a dessert called 
            gesztenyepüré – chestnut purée.","originalName":"In Hungarian cuisine, cooked chestnuts are puréed, 
            mixed with sugar (and usually rum), forced through a ricer, and topped with whipped cream to make a 
            dessert called gesztenyepüré – chestnut purée","meta":["mixed","with sugar (and usually rum), 
            forced through a ricer, and topped with whipped cream to make a dessert called gesztenyepüré - chestnut 
            purée.","cooked"],"extendedName":"cooked mixed in hungarian cuisine",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/paprika.jpg"}],"usedIngredients":[{"id":20444,
            "amount":1.0,"unit":"serving","unitLong":"serving","unitShort":"serving","aisle":"Pasta and Rice",
            "name":"chestnut is japan's most ancient fruit. kuri was cultivated even before growing rice",
            "original":"Chestnut (Kuri in Japanese) is Japan's most ancient fruit. Kuri was cultivated even before 
            growing rice.","originalName":"Chestnut (Kuri in Japanese) is Japan's most ancient fruit. Kuri was 
            cultivated even before growing rice","meta":["(Kuri in Japanese)"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/uncooked-white-rice.png"}],"unusedIngredients":[
            ]},{"vegetarian":true,"vegan":true,"glutenFree":true,"dairyFree":true,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":9,"gaps":"no","lowFodmap":true,
            "aggregateLikes":1,"spoonacularScore":69.0,"healthScore":19.0,"creditsText":"Foodista.com – The Cooking 
            Encyclopedia Everyone Can Edit","license":"CC BY 3.0","sourceName":"Foodista","pricePerServing":72.94,
            "extendedIngredients":[{"id":11206,"aisle":"Produce","image":"cucumber.jpg","consistency":"solid",
            "name":"cucumber","nameClean":"cucumber","original":"2 Japanese cucumber, cut into long sticks",
            "originalName":"Japanese cucumber, cut into long sticks","amount":2.0,"unit":"","meta":["cut into long 
            sticks"],"measures":{"us":{"amount":2.0,"unitShort":"","unitLong":""},"metric":{"amount":2.0,
            "unitShort":"","unitLong":""}}},{"id":11446,"aisle":"Ethnic Foods","image":"nori.jpg",
            "consistency":"solid","name":"nori","nameClean":"nori","original":"4 inches sheets of nori (dried 
            seaweed), cut half","originalName":"inches sheets of nori (dried seaweed), cut half","amount":4.0,
            "unit":"inches sheets","meta":["dried","( seaweed)"],"measures":{"us":{"amount":4.0,"unitShort":"inches 
            sheets","unitLong":"inches sheets"},"metric":{"amount":4.0,"unitShort":"inches sheets","unitLong":"inches 
            sheets"}}},{"id":10220054,"aisle":"Pasta and Rice","image":"uncooked-white-rice.png",
            "consistency":"solid","name":"sushi rice","nameClean":"sushi rice","original":"4 cups sushi rice",
            "originalName":"sushi rice","amount":4.0,"unit":"cups","meta":[],"measures":{"us":{"amount":4.0,
            "unitShort":"cups","unitLong":"cups"},"metric":{"amount":946.352,"unitShort":"ml",
            "unitLong":"milliliters"}}}],"id":648742,"title":"Kappa Maki","readyInMinutes":45,"servings":8,
            "sourceUrl":"http://www.foodista.com/recipe/VJ3JTZWL/kappa-maki",
            "image":"https://spoonacular.com/recipeImages/648742-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":351.69,"unit":"kcal","percentOfDailyNeeds":17.58},{"name":"Fat",
            "amount":0.63,"unit":"g","percentOfDailyNeeds":0.97},{"name":"Saturated Fat","amount":0.11,"unit":"g",
            "percentOfDailyNeeds":0.71},{"name":"Carbohydrates","amount":77.24,"unit":"g",
            "percentOfDailyNeeds":25.75},{"name":"Net Carbohydrates","amount":74.12,"unit":"g",
            "percentOfDailyNeeds":26.95},{"name":"Sugar","amount":1.04,"unit":"g","percentOfDailyNeeds":1.16},
            {"name":"Cholesterol","amount":0.0,"unit":"mg","percentOfDailyNeeds":0.0},{"name":"Sodium","amount":8.58,
            "unit":"mg","percentOfDailyNeeds":0.37},{"name":"Protein","amount":6.82,"unit":"g",
            "percentOfDailyNeeds":13.63},{"name":"Manganese","amount":0.97,"unit":"mg","percentOfDailyNeeds":48.41},
            {"name":"Selenium","amount":14.05,"unit":"µg","percentOfDailyNeeds":20.07},{"name":"Vitamin B1",
            "amount":0.19,"unit":"mg","percentOfDailyNeeds":12.73},{"name":"Fiber","amount":3.12,"unit":"g",
            "percentOfDailyNeeds":12.48},{"name":"Copper","amount":0.21,"unit":"mg","percentOfDailyNeeds":10.74},
            {"name":"Vitamin B3","amount":2.03,"unit":"mg","percentOfDailyNeeds":10.15},{"name":"Vitamin B5",
            "amount":0.95,"unit":"mg","percentOfDailyNeeds":9.49},{"name":"Iron","amount":1.67,"unit":"mg",
            "percentOfDailyNeeds":9.27},{"name":"Zinc","amount":1.25,"unit":"mg","percentOfDailyNeeds":8.34},
            {"name":"Phosphorus","amount":82.16,"unit":"mg","percentOfDailyNeeds":8.22},{"name":"Magnesium",
            "amount":30.3,"unit":"mg","percentOfDailyNeeds":7.58},{"name":"Vitamin B6","amount":0.14,"unit":"mg",
            "percentOfDailyNeeds":6.96},{"name":"Vitamin K","amount":5.45,"unit":"µg","percentOfDailyNeeds":5.19},
            {"name":"Potassium","amount":177.75,"unit":"mg","percentOfDailyNeeds":5.08},{"name":"Folate",
            "amount":18.83,"unit":"µg","percentOfDailyNeeds":4.71},{"name":"Vitamin B2","amount":0.08,"unit":"mg",
            "percentOfDailyNeeds":4.43},{"name":"Vitamin C","amount":2.9,"unit":"mg","percentOfDailyNeeds":3.51},
            {"name":"Vitamin A","amount":120.07,"unit":"IU","percentOfDailyNeeds":2.4},{"name":"Calcium",
            "amount":21.56,"unit":"mg","percentOfDailyNeeds":2.16}],"properties":[{"name":"Glycemic Index",
            "amount":12.25,"unit":""},{"name":"Glycemic Load","amount":60.72,"unit":""}],"flavonoids":[{
            "name":"Cyanidin","amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,"unit":""},
            {"name":"Delphinidin","amount":0.0,"unit":""},{"name":"Malvidin","amount":0.0,"unit":""},
            {"name":"Pelargonidin","amount":0.0,"unit":""},{"name":"Peonidin","amount":0.0,"unit":""},
            {"name":"Catechin","amount":0.0,"unit":""},{"name":"Epigallocatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin","amount":0.0,"unit":""},{"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},
            {"name":"Epigallocatechin 3-gallate","amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,
            "unit":""},{"name":"Thearubigins","amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},
            {"name":"Hesperetin","amount":0.0,"unit":""},{"name":"Naringenin","amount":0.0,"unit":""},
            {"name":"Apigenin","amount":0.0,"unit":""},{"name":"Luteolin","amount":0.0,"unit":""},
            {"name":"Isorhamnetin","amount":0.0,"unit":""},{"name":"Kaempferol","amount":0.0,"unit":""},
            {"name":"Myricetin","amount":0.0,"unit":""},{"name":"Quercetin","amount":0.0,"unit":""},
            {"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,
            "unit":""}],"ingredients":[{"id":11206,"name":"cucumber","amount":0.25,"unit":"","nutrients":[{
            "name":"Vitamin B3","amount":0.03,"unit":"mg"},{"name":"Folate","amount":10.5,"unit":"µg"},
            {"name":"Sugar","amount":1.03,"unit":"g"},{"name":"Magnesium","amount":9.0,"unit":"mg"},{"name":"Zinc",
            "amount":0.13,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.04,"unit":"mg"},{"name":"Vitamin E","amount":0.02,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.02,"unit":"mg"},{"name":"Vitamin A",
            "amount":54.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Fluoride",
            "amount":0.98,"unit":"mg"},{"name":"Manganese","amount":0.05,"unit":"mg"},{"name":"Vitamin C",
            "amount":2.4,"unit":"mg"},{"name":"Selenium","amount":0.08,"unit":"µg"},{"name":"Net Carbohydrates",
            "amount":1.1,"unit":"g"},{"name":"Vitamin B5","amount":0.18,"unit":"mg"},{"name":"Vitamin K",
            "amount":5.4,"unit":"µg"},{"name":"Saturated Fat","amount":0.01,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.02,"unit":"mg"},{"name":"Fiber","amount":0.53,
            "unit":"g"},{"name":"Iron","amount":0.17,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":15.75,"unit":"mg"},{"name":"Carbohydrates","amount":1.62,"unit":"g"},
            {"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":1.5,"unit":"mg"},
            {"name":"Calcium","amount":10.5,"unit":"mg"},{"name":"Potassium","amount":102.0,"unit":"mg"},
            {"name":"Choline","amount":4.28,"unit":"mg"},{"name":"Calories","amount":9.0,"unit":"kcal"},
            {"name":"Copper","amount":0.05,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.44,"unit":"g"},{"name":"Fat","amount":0.12,"unit":"g"}]},{"id":11446,
            "name":"nori","amount":0.5,"unit":"inches sheets","nutrients":[{"name":"Vitamin B3","amount":0.02,
            "unit":"mg"},{"name":"Folate","amount":1.85,"unit":"µg"},{"name":"Sugar","amount":0.01,"unit":"g"},
            {"name":"Magnesium","amount":0.03,"unit":"mg"},{"name":"Zinc","amount":0.01,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            E","amount":0.01,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":66.07,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Manganese","amount":0.01,"unit":"mg"},{"name":"Vitamin C","amount":0.5,
            "unit":"mg"},{"name":"Selenium","amount":0.01,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.06,
            "unit":"g"},{"name":"Vitamin B5","amount":0.01,"unit":"mg"},{"name":"Vitamin K","amount":0.05,
            "unit":"µg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.01,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.02,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus",
            "amount":0.74,"unit":"mg"},{"name":"Carbohydrates","amount":0.06,"unit":"g"},{"name":"Lycopene",
            "amount":0.0,"unit":"µg"},{"name":"Sodium","amount":0.61,"unit":"mg"},{"name":"Calcium","amount":0.89,
            "unit":"mg"},{"name":"Potassium","amount":4.52,"unit":"mg"},{"name":"Choline","amount":0.13,"unit":"mg"},
            {"name":"Calories","amount":0.44,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.07,"unit":"g"},{"name":"Fat","amount":0.0,
            "unit":"g"}]},{"id":10220054,"name":"sushi rice","amount":0.5,"unit":"cups","nutrients":[{"name":"Vitamin 
            B3","amount":1.98,"unit":"mg"},{"name":"Folate","amount":6.48,"unit":"µg"},{"name":"Magnesium",
            "amount":21.28,"unit":"mg"},{"name":"Zinc","amount":1.11,"unit":"mg"},{"name":"Poly Unsaturated Fat",
            "amount":0.18,"unit":"g"},{"name":"Vitamin B6","amount":0.1,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.17,"unit":"mg"},{"name":"Vitamin A",
            "amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.19,"unit":"g"},{"name":"Manganese",
            "amount":0.9,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":13.97,"unit":"µg"},{"name":"Net Carbohydrates","amount":72.96,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.76,"unit":"mg"},{"name":"Saturated Fat","amount":0.1,"unit":"g"},{"name":"Vitamin B2",
            "amount":0.05,"unit":"mg"},{"name":"Fiber","amount":2.59,"unit":"g"},{"name":"Iron","amount":1.48,
            "unit":"mg"},{"name":"Phosphorus","amount":65.68,"unit":"mg"},{"name":"Carbohydrates","amount":75.55,
            "unit":"g"},{"name":"Sodium","amount":6.48,"unit":"mg"},{"name":"Calcium","amount":10.18,"unit":"mg"},
            {"name":"Potassium","amount":71.22,"unit":"mg"},{"name":"Calories","amount":342.25,"unit":"kcal"},
            {"name":"Copper","amount":0.16,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":6.3,"unit":"g"},{"name":"Fat","amount":0.51,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":7.97,"percentFat":1.66,"percentCarbs":90.37},"weightPerServing":{
            "amount":169,"unit":"g"}},"summary":"Kappa Maki might be just the side dish you are searching for. One 
            serving contains <b>351 calories</b>, <b>7g of protein</b>, and <b>1g of fat</b>. This recipe serves 8 
            and costs 70 cents per serving. Head to the store and pick up japanese cucumber, of nori, sushi rice, 
            and a few other things to make it today. 1 person has tried and liked this recipe. It is a good option if 
            you're following a <b>gluten free, fodmap friendly, and vegan</b> diet. From preparation to the plate, 
            this recipe takes about <b>45 minutes</b>. All things considered, we decided this recipe <b>deserves a 
            spoonacular score of 70%</b>. This score is good. Try <a 
            href=\"https://spoonacular.com/recipes/kappa-maki-cucumber-sushi-roll-565133\">Kappa Maki (Cucumber Sushi 
            Roll)</a>, <a href=\"https://spoonacular.com/recipes/live-sigma-kappa-elvis-cookies-508466\">Live Sigma 
            Kappa – Elvis Cookies</a>, and <a 
            href=\"https://spoonacular.com/recipes/live-sigma-kappa-texas-caviar-508442\">Live Sigma Kappa – Texas 
            Caviar</a> for similar recipes.","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free",
            "dairy free","lacto ovo vegetarian","fodmap friendly","vegan"],"occasions":[],"analyzedInstructions":[{
            "name":"","steps":[{"number":1,"step":"Put a half-size nori on top of a bamboo mat (makisu).",
            "ingredients":[{"id":11446,"name":"nori","localizedName":"nori","image":"nori.jpg"}],"equipment":[]},
            {"number":2,"step":"Spread a half cup of sushi rice on top.","ingredients":[{"id":10220054,"name":"sushi 
            rice","localizedName":"sushi rice","image":"uncooked-white-rice.png"},{"id":0,"name":"spread",
            "localizedName":"spread","image":""}],"equipment":[]},{"number":3,"step":"Place cucumber sticks 
            lengthwise on the rice.","ingredients":[{"id":11206,"name":"cucumber","localizedName":"cucumber",
            "image":"cucumber.jpg"},{"id":20444,"name":"rice","localizedName":"rice",
            "image":"uncooked-white-rice.png"}],"equipment":[]},{"number":4,"step":"Roll up the bamboo mat, 
            pressing forward to shape the sushi into a cylinder. Press the bamboo mat firmly with hands.Unwrap the 
            bamboo mat.","ingredients":[{"id":0,"name":"roll","localizedName":"roll",
            "image":"dinner-yeast-rolls.jpg"}],"equipment":[]},{"number":5,"step":"Cut the sushi roll into bite-size 
            pieces.","ingredients":[{"id":0,"name":"roll","localizedName":"roll","image":"dinner-yeast-rolls.jpg"}],
            "equipment":[]}]}],"spoonacularSourceUrl":"https://spoonacular.com/kappa-maki-648742",
            "usedIngredientCount":1,"missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":11206,
            "amount":2.0,"unit":"","unitLong":"","unitShort":"","aisle":"Produce","name":"cucumber","original":"2 
            Japanese cucumber, cut into long sticks","originalName":"Japanese cucumber, cut into long sticks",
            "meta":["cut into long sticks"],"image":"https://spoonacular.com/cdn/ingredients_100x100/cucumber.jpg"},
            {"id":11446,"amount":4.0,"unit":"inches sheets","unitLong":"inches sheets","unitShort":"inches sheets",
            "aisle":"Ethnic Foods","name":"nori","original":"4 inches sheets of nori (dried seaweed), cut half",
            "originalName":"inches sheets of nori (dried seaweed), cut half","meta":["dried","( seaweed)"],
            "extendedName":"dried nori","image":"https://spoonacular.com/cdn/ingredients_100x100/nori.jpg"}],
            "usedIngredients":[{"id":10220054,"amount":4.0,"unit":"cups","unitLong":"cups","unitShort":"cup",
            "aisle":"Pasta and Rice","name":"sushi rice","original":"4 cups sushi rice","originalName":"sushi rice",
            "meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/uncooked-white-rice.png"}],
            "unusedIngredients":[]},{"vegetarian":true,"vegan":true,"glutenFree":true,"dairyFree":true,
            "veryHealthy":false,"cheap":false,"veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":16,
            "gaps":"no","lowFodmap":true,"aggregateLikes":1,"spoonacularScore":48.0,"healthScore":10.0,
            "creditsText":"Foodista.com – The Cooking Encyclopedia Everyone Can Edit","license":"CC BY 3.0",
            "sourceName":"Foodista","pricePerServing":90.56,"extendedIngredients":[{"id":20444,"aisle":"Pasta and 
            Rice","image":"uncooked-white-rice.png","consistency":"solid","name":"rice","nameClean":"rice",
            "original":"2 cups white rice - wash and drain off excess water","originalName":"white rice - wash and 
            drain off excess water","amount":2.0,"unit":"cups","meta":["white"],"measures":{"us":{"amount":2.0,
            "unitShort":"cups","unitLong":"cups"},"metric":{"amount":473.176,"unitShort":"ml",
            "unitLong":"milliliters"}}},{"id":2064,"aisle":"Produce;Spices and Seasonings","image":"mint.jpg",
            "consistency":"solid","name":"mint leaves","nameClean":"mint","original":"1 small bunch mint leaves (1 
            cup)","originalName":"small bunch mint leaves","amount":1.0,"unit":"cup","meta":[],"measures":{"us":{
            "amount":1.0,"unitShort":"cup","unitLong":"cup"},"metric":{"amount":236.588,"unitShort":"ml",
            "unitLong":"milliliters"}}},{"id":12118,"aisle":"Canned and Jarred;Milk, Eggs, Other Dairy",
            "image":"coconut-milk.png","consistency":"liquid","name":"coconut milk","nameClean":"coconut milk",
            "original":"1 cup coconut milk (can replace with cream or carton milk)","originalName":"coconut milk (can 
            replace with cream or carton milk)","amount":1.0,"unit":"cup","meta":["with cream or carton milk)"],
            "measures":{"us":{"amount":1.0,"unitShort":"cup","unitLong":"cup"},"metric":{"amount":236.588,
            "unitShort":"ml","unitLong":"milliliters"}}},{"id":2047,"aisle":"Spices and Seasonings",
            "image":"salt.jpg","consistency":"solid","name":"salt","nameClean":"table salt","original":"Salt to 
            taste","originalName":"Salt to taste","amount":1.0,"unit":"serving","meta":["to taste"],"measures":{
            "us":{"amount":1.0,"unitShort":"serving","unitLong":"serving"},"metric":{"amount":1.0,
            "unitShort":"serving","unitLong":"serving"}}},{"id":14412,"aisle":"Beverages","image":"water.png",
            "consistency":"liquid","name":"water","nameClean":"water","original":"2 cups water.",
            "originalName":"water","amount":2.0,"unit":"cups","meta":[],"measures":{"us":{"amount":2.0,
            "unitShort":"cups","unitLong":"cups"},"metric":{"amount":473.176,"unitShort":"ml",
            "unitLong":"milliliters"}}}],"id":652965,"title":"Nasi Pudina (Mint Rice)","readyInMinutes":45,
            "servings":4,"sourceUrl":"https://www.foodista.com/recipe/L4Z2WWHS/nasi-pudina-mint-rice",
            "image":"https://spoonacular.com/recipeImages/652965-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":456.81,"unit":"kcal","percentOfDailyNeeds":22.84},{"name":"Fat",
            "amount":12.77,"unit":"g","percentOfDailyNeeds":19.64},{"name":"Saturated Fat","amount":10.88,"unit":"g",
            "percentOfDailyNeeds":68.01},{"name":"Carbohydrates","amount":77.22,"unit":"g",
            "percentOfDailyNeeds":25.74},{"name":"Net Carbohydrates","amount":75.11,"unit":"g",
            "percentOfDailyNeeds":27.31},{"name":"Sugar","amount":0.11,"unit":"g","percentOfDailyNeeds":0.12},
            {"name":"Cholesterol","amount":0.0,"unit":"mg","percentOfDailyNeeds":0.0},{"name":"Sodium",
            "amount":69.82,"unit":"mg","percentOfDailyNeeds":3.04},{"name":"Protein","amount":8.16,"unit":"g",
            "percentOfDailyNeeds":16.32},{"name":"Manganese","amount":1.57,"unit":"mg","percentOfDailyNeeds":78.64},
            {"name":"Selenium","amount":13.97,"unit":"µg","percentOfDailyNeeds":19.95},{"name":"Copper",
            "amount":0.39,"unit":"mg","percentOfDailyNeeds":19.27},{"name":"Iron","amount":3.18,"unit":"mg",
            "percentOfDailyNeeds":17.65},{"name":"Phosphorus","amount":168.83,"unit":"mg",
            "percentOfDailyNeeds":16.88},{"name":"Magnesium","amount":59.3,"unit":"mg","percentOfDailyNeeds":14.82},
            {"name":"Vitamin B5","amount":1.06,"unit":"mg","percentOfDailyNeeds":10.62},{"name":"Vitamin B3",
            "amount":2.03,"unit":"mg","percentOfDailyNeeds":10.16},{"name":"Zinc","amount":1.46,"unit":"mg",
            "percentOfDailyNeeds":9.74},{"name":"Vitamin A","amount":477.9,"unit":"IU","percentOfDailyNeeds":9.56},
            {"name":"Vitamin B6","amount":0.18,"unit":"mg","percentOfDailyNeeds":9.1},{"name":"Potassium",
            "amount":294.7,"unit":"mg","percentOfDailyNeeds":8.42},{"name":"Fiber","amount":2.1,"unit":"g",
            "percentOfDailyNeeds":8.41},{"name":"Folate","amount":28.14,"unit":"µg","percentOfDailyNeeds":7.03},
            {"name":"Calcium","amount":66.99,"unit":"mg","percentOfDailyNeeds":6.7},{"name":"Vitamin B1",
            "amount":0.09,"unit":"mg","percentOfDailyNeeds":5.76},{"name":"Vitamin C","amount":4.14,"unit":"mg",
            "percentOfDailyNeeds":5.02},{"name":"Vitamin B2","amount":0.08,"unit":"mg","percentOfDailyNeeds":4.43}],
            "properties":[{"name":"Glycemic Index","amount":39.55,"unit":""},{"name":"Glycemic Load","amount":46.05,
            "unit":""}],"flavonoids":[{"name":"Cyanidin","amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,
            "unit":""},{"name":"Delphinidin","amount":0.0,"unit":""},{"name":"Malvidin","amount":0.0,"unit":""},
            {"name":"Pelargonidin","amount":0.0,"unit":""},{"name":"Peonidin","amount":0.0,"unit":""},
            {"name":"Catechin","amount":0.0,"unit":""},{"name":"Epigallocatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin","amount":0.0,"unit":""},{"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},
            {"name":"Epigallocatechin 3-gallate","amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,
            "unit":""},{"name":"Thearubigins","amount":0.0,"unit":""},{"name":"Eriodictyol","amount":3.48,
            "unit":"mg"},{"name":"Hesperetin","amount":1.14,"unit":"mg"},{"name":"Naringenin","amount":0.0,
            "unit":""},{"name":"Apigenin","amount":0.61,"unit":"mg"},{"name":"Luteolin","amount":1.42,"unit":"mg"},
            {"name":"Isorhamnetin","amount":0.0,"unit":"mg"},{"name":"Kaempferol","amount":0.0,"unit":"mg"},
            {"name":"Myricetin","amount":0.0,"unit":""},{"name":"Quercetin","amount":0.0,"unit":"mg"},
            {"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,
            "unit":""}],"ingredients":[{"id":20444,"name":"rice","amount":0.5,"unit":"cups","nutrients":[{
            "name":"Vitamin B3","amount":1.48,"unit":"mg"},{"name":"Folate","amount":7.4,"unit":"µg"},
            {"name":"Sugar","amount":0.11,"unit":"g"},{"name":"Magnesium","amount":23.13,"unit":"mg"},{"name":"Zinc",
            "amount":1.01,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.16,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.15,"unit":"mg"},{"name":"Vitamin E","amount":0.1,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.06,"unit":"mg"},{"name":"Vitamin A",
            "amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.19,"unit":"g"},{"name":"Manganese",
            "amount":1.01,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":13.97,"unit":"µg"},{"name":"Net Carbohydrates","amount":72.75,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.94,"unit":"mg"},{"name":"Vitamin K","amount":0.09,"unit":"µg"},{"name":"Saturated Fat",
            "amount":0.17,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.05,
            "unit":"mg"},{"name":"Fiber","amount":1.2,"unit":"g"},{"name":"Iron","amount":0.74,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":106.38,"unit":"mg"},
            {"name":"Carbohydrates","amount":73.95,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},
            {"name":"Sodium","amount":4.63,"unit":"mg"},{"name":"Calcium","amount":25.9,"unit":"mg"},
            {"name":"Potassium","amount":106.38,"unit":"mg"},{"name":"Choline","amount":5.37,"unit":"mg"},
            {"name":"Calories","amount":337.63,"unit":"kcal"},{"name":"Copper","amount":0.2,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":6.6,"unit":"g"},{"name":"Fat",
            "amount":0.61,"unit":"g"}]},{"id":2064,"name":"mint leaves","amount":0.25,"unit":"cup","nutrients":[{
            "name":"Vitamin B3","amount":0.19,"unit":"mg"},{"name":"Folate","amount":12.83,"unit":"µg"},
            {"name":"Magnesium","amount":9.0,"unit":"mg"},{"name":"Zinc","amount":0.12,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.06,"unit":"g"},{"name":"Vitamin B6","amount":0.01,"unit":"mg"},
            {"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.01,"unit":"mg"},
            {"name":"Vitamin A","amount":477.9,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},
            {"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},
            {"name":"Manganese","amount":0.13,"unit":"mg"},{"name":"Vitamin C","amount":3.58,"unit":"mg"},
            {"name":"Net Carbohydrates","amount":0.78,"unit":"g"},{"name":"Vitamin B5","amount":0.04,"unit":"mg"},
            {"name":"Saturated Fat","amount":0.03,"unit":"g"},{"name":"Vitamin B2","amount":0.03,"unit":"mg"},
            {"name":"Fiber","amount":0.9,"unit":"g"},{"name":"Iron","amount":0.57,"unit":"mg"},{"name":"Phosphorus",
            "amount":8.21,"unit":"mg"},{"name":"Carbohydrates","amount":1.68,"unit":"g"},{"name":"Sodium",
            "amount":3.49,"unit":"mg"},{"name":"Calcium","amount":27.34,"unit":"mg"},{"name":"Potassium",
            "amount":64.01,"unit":"mg"},{"name":"Calories","amount":7.88,"unit":"kcal"},{"name":"Copper",
            "amount":0.04,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein",
            "amount":0.42,"unit":"g"},{"name":"Fat","amount":0.11,"unit":"g"}]},{"id":12118,"name":"coconut milk",
            "amount":0.25,"unit":"cup","nutrients":[{"name":"Vitamin B3","amount":0.36,"unit":"mg"},{"name":"Folate",
            "amount":7.91,"unit":"µg"},{"name":"Magnesium","amount":25.99,"unit":"mg"},{"name":"Zinc","amount":0.32,
            "unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.13,"unit":"g"},{"name":"Vitamin B6","amount":0.02,
            "unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.01,
            "unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,
            "unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.51,"unit":"g"},{"name":"Manganese","amount":0.43,"unit":"mg"},{"name":"Vitamin C",
            "amount":0.56,"unit":"mg"},{"name":"Net Carbohydrates","amount":1.59,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.09,"unit":"mg"},{"name":"Saturated Fat","amount":10.69,"unit":"g"},{"name":"Vitamin B2",
            "amount":0.0,"unit":"mg"},{"name":"Iron","amount":1.86,"unit":"mg"},{"name":"Phosphorus","amount":54.24,
            "unit":"mg"},{"name":"Carbohydrates","amount":1.59,"unit":"g"},{"name":"Sodium","amount":7.35,
            "unit":"mg"},{"name":"Calcium","amount":10.17,"unit":"mg"},{"name":"Potassium","amount":124.3,
            "unit":"mg"},{"name":"Choline","amount":4.8,"unit":"mg"},{"name":"Calories","amount":111.31,
            "unit":"kcal"},{"name":"Copper","amount":0.13,"unit":"mg"},{"name":"Folic Acid","amount":0.0,
            "unit":"µg"},{"name":"Protein","amount":1.14,"unit":"g"},{"name":"Fat","amount":12.05,"unit":"g"}]},
            {"id":2047,"name":"salt","amount":0.25,"unit":"serving","nutrients":[{"name":"Vitamin B3","amount":0.0,
            "unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.0,"unit":"g"},
            {"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},{"name":"Vitamin B12",
            "amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,"unit":"mg"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium","amount":0.0,"unit":"µg"},
            {"name":"Net Carbohydrates","amount":0.0,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},
            {"name":"Vitamin K","amount":0.0,"unit":"µg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},
            {"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},
            {"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":0.0,"unit":"mg"},{"name":"Caffeine",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},{"name":"Sodium","amount":48.45,
            "unit":"mg"},{"name":"Calcium","amount":0.03,"unit":"mg"},{"name":"Potassium","amount":0.01,"unit":"mg"},
            {"name":"Choline","amount":0.0,"unit":"mg"},{"name":"Calories","amount":0.0,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic Acid","amount":0.0,"unit":"µg"},
            {"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]},{"id":14412,
            "name":"water","amount":0.5,"unit":"cups","nutrients":[{"name":"Fiber","amount":0.0,"unit":"g"},
            {"name":"Magnesium","amount":1.18,"unit":"mg"},{"name":"Zinc","amount":0.01,"unit":"mg"},{"name":"Iron",
            "amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.0,"unit":"g"},{"name":"Sodium","amount":5.91,"unit":"mg"},{"name":"Calcium","amount":3.55,
            "unit":"mg"},{"name":"Fluoride","amount":30.52,"unit":"mg"},{"name":"Manganese","amount":0.0,
            "unit":"mg"},{"name":"Potassium","amount":0.0,"unit":"mg"},{"name":"Calories","amount":0.0,
            "unit":"kcal"},{"name":"Copper","amount":0.02,"unit":"mg"},{"name":"Net Carbohydrates","amount":0.0,
            "unit":"g"},{"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":7.15,"percentFat":25.18,"percentCarbs":67.67},"weightPerServing":{
            "amount":279,"unit":"g"}},"summary":"If you have about <b>around 45 minutes</b> to spend in the kitchen, 
            Nasi Pudina (Mint Rice) might be a great <b>gluten free, dairy free, lacto ovo vegetarian, and fodmap 
            friendly</b> recipe to try. This recipe serves 4. For <b>91 cents per serving</b>, this recipe <b>covers 
            11%</b> of your daily requirements of vitamins and minerals. This side dish has <b>457 calories</b>, 
            <b>8g of protein</b>, and <b>13g of fat</b> per serving. Head to the store and pick up rice - wash and 
            drain off excess water, mint leaves, water, and a few other things to make it today. 1 person were glad 
            they tried this recipe. It is brought to you by Foodista. With a spoonacular <b>score of 46%</b>, 
            this dish is solid. Similar recipes are <a 
            href=\"https://spoonacular.com/recipes/pudina-rice-or-mint-pulao-618730\">Pudina Rice or Mint Pulao</a>, 
            <a href=\"https://spoonacular.com/recipes/pudina-dal-or-mint-dal-pudina-moong-dal-487597\">pudina dal or 
            mint dal | pudina moong dal</a>, and <a 
            href=\"https://spoonacular.com/recipes/mint-tea-or-pudina-chai-how-to-make-mint-tea-486778\">Mint Tean or 
            Pudina Chai , How to make Mint Tea</a>.","cuisines":[],"dishTypes":["side dish"],"diets":["gluten free",
            "dairy free","lacto ovo vegetarian","fodmap friendly","vegan"],"occasions":[],"analyzedInstructions":[{
            "name":"","steps":[{"number":1,"step":"Blend mint leaves with coconut milk till smooth.","ingredients":[{
            "id":12118,"name":"coconut milk","localizedName":"coconut milk","image":"coconut-milk.png"},{"id":2064,
            "name":"mint","localizedName":"mint","image":"mint.jpg"}],"equipment":[]},{"number":2,"step":"Pour into 
            rice cooker.","ingredients":[{"id":20444,"name":"rice","localizedName":"rice",
            "image":"uncooked-white-rice.png"}],"equipment":[{"id":404662,"name":"rice cooker","localizedName":"rice 
            cooker","image":"rice-cooker.jpg"}]},{"number":3,"step":"Add rice, water and salt.","ingredients":[{
            "id":14412,"name":"water","localizedName":"water","image":"water.png"},{"id":20444,"name":"rice",
            "localizedName":"rice","image":"uncooked-white-rice.png"},{"id":2047,"name":"salt",
            "localizedName":"salt","image":"salt.jpg"}],"equipment":[]},{"number":4,"step":"Switch on and once rice 
            is cooked. gently fluff up with a fork/chopsticks.","ingredients":[{"id":20444,"name":"rice",
            "localizedName":"rice","image":"uncooked-white-rice.png"}],"equipment":[{"id":405596,"name":"chopsticks",
            "localizedName":"chopsticks","image":"chopsticks.jpg"}]},{"number":5,"step":"Optional: For the crunch, 
            sprinkle roasted peanuts before serving.","ingredients":[{"id":16092,"name":"roasted peanuts",
            "localizedName":"roasted peanuts","image":"peanuts.png"}],"equipment":[]}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/nasi-pudina-mint-rice-652965","usedIngredientCount":1,
            "missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":2064,"amount":1.0,"unit":"cup",
            "unitLong":"cup","unitShort":"cup","aisle":"Produce;Spices and Seasonings","name":"mint leaves",
            "original":"1 small bunch mint leaves (1 cup)","originalName":"small bunch mint leaves","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/mint.jpg"},{"id":12118,"amount":1.0,
            "unit":"cup","unitLong":"cup","unitShort":"cup","aisle":"Canned and Jarred;Milk, Eggs, Other Dairy",
            "name":"coconut milk","original":"1 cup coconut milk (can replace with cream or carton milk)",
            "originalName":"coconut milk (can replace with cream or carton milk)","meta":["with cream or carton 
            milk)"],"image":"https://spoonacular.com/cdn/ingredients_100x100/coconut-milk.png"}],"usedIngredients":[{
            "id":20444,"amount":2.0,"unit":"cups","unitLong":"cups","unitShort":"cup","aisle":"Pasta and Rice",
            "name":"rice","original":"2 cups white rice - wash and drain off excess water","originalName":"white rice 
            - wash and drain off excess water","meta":["white"],"extendedName":"white rice",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/uncooked-white-rice.png"}],"unusedIngredients":[
            ]},{"vegetarian":true,"vegan":true,"glutenFree":true,"dairyFree":true,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":12,"gaps":"no","lowFodmap":true,
            "aggregateLikes":1,"spoonacularScore":18.0,"healthScore":1.0,"creditsText":"Foodista.com – The Cooking 
            Encyclopedia Everyone Can Edit","license":"CC BY 3.0","sourceName":"Foodista","pricePerServing":87.36,
            "extendedIngredients":[{"id":10020036,"aisle":"Pasta and Rice","image":"black-rice.jpg",
            "consistency":"solid","name":"black rice","nameClean":"black rice","original":"1⁄3 cup long-grain black 
            rice","originalName":"long-grain black rice","amount":0.3333333333333333,"unit":"cup",
            "meta":["long-grain","black"],"measures":{"us":{"amount":0.333,"unitShort":"cups","unitLong":"cups"},
            "metric":{"amount":78.863,"unitShort":"ml","unitLong":"milliliters"}}},{"id":99009,"aisle":"Canned and 
            Jarred","image":"coconut-milk.jpg","consistency":"liquid","name":"light coconut milk","nameClean":"light 
            coconut milk","original":"1 14-ounce cans light coconut milk","originalName":"light coconut milk",
            "amount":14.0,"unit":"ounce","meta":["light","canned"],"measures":{"us":{"amount":14.0,"unitShort":"oz",
            "unitLong":"ounces"},"metric":{"amount":396.893,"unitShort":"g","unitLong":"grams"}}},{"id":19334,
            "aisle":"Baking","image":"dark-brown-sugar.png","consistency":"solid","name":"brown sugar",
            "nameClean":"golden brown sugar","original":"1⁄2 cup brown sugar","originalName":"brown sugar",
            "amount":0.5,"unit":"cup","meta":[],"measures":{"us":{"amount":0.5,"unitShort":"cups","unitLong":"cups"},
            "metric":{"amount":118.294,"unitShort":"ml","unitLong":"milliliters"}}},{"id":2047,"aisle":"Spices and 
            Seasonings","image":"salt.jpg","consistency":"solid","name":"salt","nameClean":"table salt",
            "original":"Pinch of salt","originalName":"Pinch of salt","amount":1.0,"unit":"pinch","meta":[],
            "measures":{"us":{"amount":1.0,"unitShort":"pinch","unitLong":"pinch"},"metric":{"amount":1.0,
            "unitShort":"pinch","unitLong":"pinch"}}},{"id":1002006,"aisle":"Spices and Seasonings",
            "image":"cardamom.jpg","consistency":"solid","name":"cardamon pods","nameClean":"cardamom pods",
            "original":"A few cardamon pods, cinnamon sticks or saffron","originalName":"A few cardamon pods, 
            cinnamon or saffron","amount":3.0,"unit":"sticks","meta":[],"measures":{"us":{"amount":3.0,
            "unitShort":"sticks","unitLong":"sticks"},"metric":{"amount":3.0,"unitShort":"sticks",
            "unitLong":"sticks"}}}],"id":637095,"title":"Cardamon Infused Black Rice Pudding with Coconut Milk",
            "readyInMinutes":45,"servings":4,
            "sourceUrl":"https://www.foodista.com/recipe/PQMPK3Y5/cardamon-infused-black-rice-pudding-with-coconut
            -milk","image":"https://spoonacular.com/recipeImages/637095-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":246.56,"unit":"kcal","percentOfDailyNeeds":12.33},{"name":"Fat",
            "amount":7.11,"unit":"g","percentOfDailyNeeds":10.94},{"name":"Saturated Fat","amount":6.7,"unit":"g",
            "percentOfDailyNeeds":41.9},{"name":"Carbohydrates","amount":42.7,"unit":"g",
            "percentOfDailyNeeds":14.23},{"name":"Net Carbohydrates","amount":41.95,"unit":"g",
            "percentOfDailyNeeds":15.26},{"name":"Sugar","amount":26.81,"unit":"g","percentOfDailyNeeds":29.78},
            {"name":"Cholesterol","amount":0.0,"unit":"mg","percentOfDailyNeeds":0.0},{"name":"Sodium",
            "amount":101.29,"unit":"mg","percentOfDailyNeeds":4.4},{"name":"Protein","amount":1.34,"unit":"g",
            "percentOfDailyNeeds":2.68},{"name":"Manganese","amount":0.8,"unit":"mg","percentOfDailyNeeds":40.23},
            {"name":"Magnesium","amount":26.24,"unit":"mg","percentOfDailyNeeds":6.56},{"name":"Selenium",
            "amount":3.94,"unit":"µg","percentOfDailyNeeds":5.63},{"name":"Phosphorus","amount":53.77,"unit":"mg",
            "percentOfDailyNeeds":5.38},{"name":"Vitamin B6","amount":0.09,"unit":"mg","percentOfDailyNeeds":4.57},
            {"name":"Vitamin B1","amount":0.06,"unit":"mg","percentOfDailyNeeds":4.22},{"name":"Vitamin B3",
            "amount":0.82,"unit":"mg","percentOfDailyNeeds":4.12},{"name":"Fiber","amount":0.75,"unit":"g",
            "percentOfDailyNeeds":3.0},{"name":"Iron","amount":0.53,"unit":"mg","percentOfDailyNeeds":2.93},
            {"name":"Copper","amount":0.06,"unit":"mg","percentOfDailyNeeds":2.93},{"name":"Calcium","amount":29.25,
            "unit":"mg","percentOfDailyNeeds":2.92},{"name":"Vitamin B5","amount":0.27,"unit":"mg",
            "percentOfDailyNeeds":2.66},{"name":"Zinc","amount":0.38,"unit":"mg","percentOfDailyNeeds":2.5},
            {"name":"Potassium","amount":79.35,"unit":"mg","percentOfDailyNeeds":2.27},{"name":"Vitamin E",
            "amount":0.19,"unit":"mg","percentOfDailyNeeds":1.23}],"properties":[{"name":"Glycemic Index",
            "amount":1.25,"unit":""},{"name":"Glycemic Load","amount":0.02,"unit":""}],"flavonoids":[{
            "name":"Cyanidin","amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,"unit":""},
            {"name":"Delphinidin","amount":0.0,"unit":""},{"name":"Malvidin","amount":0.0,"unit":""},
            {"name":"Pelargonidin","amount":0.0,"unit":""},{"name":"Peonidin","amount":0.0,"unit":""},
            {"name":"Catechin","amount":0.0,"unit":""},{"name":"Epigallocatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin","amount":0.0,"unit":""},{"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},
            {"name":"Epigallocatechin 3-gallate","amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,
            "unit":""},{"name":"Thearubigins","amount":0.0,"unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},
            {"name":"Hesperetin","amount":0.0,"unit":""},{"name":"Naringenin","amount":0.0,"unit":""},
            {"name":"Apigenin","amount":0.0,"unit":""},{"name":"Luteolin","amount":0.0,"unit":""},
            {"name":"Isorhamnetin","amount":0.0,"unit":""},{"name":"Kaempferol","amount":0.0,"unit":""},
            {"name":"Myricetin","amount":0.0,"unit":""},{"name":"Quercetin","amount":0.0,"unit":""},
            {"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},{"name":"Theaflavin-3'-gallate","amount":0.0,
            "unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,"unit":""},{"name":"Gallocatechin","amount":0.0,
            "unit":""}],"ingredients":[{"id":10020036,"name":"black rice","amount":0.08,"unit":"cup","nutrients":[{
            "name":"Vitamin B3","amount":0.78,"unit":"mg"},{"name":"Folate","amount":3.08,"unit":"µg"},
            {"name":"Sugar","amount":0.13,"unit":"g"},{"name":"Magnesium","amount":22.05,"unit":"mg"},{"name":"Zinc",
            "amount":0.31,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.16,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.08,"unit":"mg"},{"name":"Vitamin E","amount":0.19,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.06,"unit":"mg"},{"name":"Vitamin A",
            "amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.16,"unit":"g"},{"name":"Manganese",
            "amount":0.58,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":3.61,"unit":"µg"},{"name":"Net Carbohydrates","amount":11.37,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.23,"unit":"mg"},{"name":"Vitamin K","amount":0.29,"unit":"µg"},{"name":"Saturated Fat",
            "amount":0.09,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.01,
            "unit":"mg"},{"name":"Fiber","amount":0.54,"unit":"g"},{"name":"Iron","amount":0.23,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":51.34,"unit":"mg"},
            {"name":"Carbohydrates","amount":11.91,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},
            {"name":"Sodium","amount":1.08,"unit":"mg"},{"name":"Calcium","amount":3.55,"unit":"mg"},
            {"name":"Potassium","amount":34.38,"unit":"mg"},{"name":"Choline","amount":4.73,"unit":"mg"},
            {"name":"Calories","amount":57.04,"unit":"kcal"},{"name":"Copper","amount":0.04,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":1.22,"unit":"g"},{"name":"Fat",
            "amount":0.45,"unit":"g"}]},{"id":99009,"name":"light coconut milk","amount":3.5,"unit":"ounce",
            "nutrients":[{"name":"Vitamin B3","amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},
            {"name":"Sugar","amount":0.0,"unit":"g"},{"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc",
            "amount":0.0,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.0,"unit":"mg"},{"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,
            "unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,
            "unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,
            "unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,
            "unit":"mg"},{"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},
            {"name":"Trans Fat","amount":0.0,"unit":"g"},{"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":3.3,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            K","amount":0.0,"unit":"µg"},{"name":"Saturated Fat","amount":6.61,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,
            "unit":"g"},{"name":"Iron","amount":0.0,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":0.0,"unit":"mg"},{"name":"Carbohydrates","amount":3.3,"unit":"g"},
            {"name":"Sodium","amount":82.68,"unit":"mg"},{"name":"Calcium","amount":0.0,"unit":"mg"},
            {"name":"Potassium","amount":0.0,"unit":"mg"},{"name":"Calories","amount":82.68,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat",
            "amount":6.61,"unit":"g"}]},{"id":19334,"name":"brown sugar","amount":0.13,"unit":"cup","nutrients":[{
            "name":"Vitamin B3","amount":0.03,"unit":"mg"},{"name":"Folate","amount":0.28,"unit":"µg"},
            {"name":"Sugar","amount":26.68,"unit":"g"},{"name":"Magnesium","amount":2.48,"unit":"mg"},{"name":"Zinc",
            "amount":0.01,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.01,"unit":"mg"},{"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A",
            "amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Manganese",
            "amount":0.02,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":0.33,"unit":"µg"},{"name":"Net Carbohydrates","amount":26.98,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.04,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},{"name":"Saturated Fat",
            "amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,
            "unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron","amount":0.2,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":1.1,"unit":"mg"},
            {"name":"Carbohydrates","amount":26.98,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},
            {"name":"Sodium","amount":7.7,"unit":"mg"},{"name":"Calcium","amount":22.83,"unit":"mg"},
            {"name":"Potassium","amount":36.58,"unit":"mg"},{"name":"Choline","amount":0.63,"unit":"mg"},
            {"name":"Calories","amount":104.5,"unit":"kcal"},{"name":"Copper","amount":0.01,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.03,"unit":"g"},{"name":"Fat",
            "amount":0.0,"unit":"g"}]},{"id":2047,"name":"salt","amount":0.25,"unit":"pinch","nutrients":[{
            "name":"Vitamin B3","amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar",
            "amount":0.0,"unit":"g"},{"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,
            "unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,
            "unit":"mg"},{"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,"unit":"mg"},
            {"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.0,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.0,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,
            "unit":"mg"},{"name":"Carbohydrates","amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,
            "unit":"µg"},{"name":"Sodium","amount":9.69,"unit":"mg"},{"name":"Calcium","amount":0.01,"unit":"mg"},
            {"name":"Potassium","amount":0.0,"unit":"mg"},{"name":"Choline","amount":0.0,"unit":"mg"},
            {"name":"Calories","amount":0.0,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,
            "unit":"g"}]},{"id":1002006,"name":"cardamon pods","amount":0.75,"unit":"sticks","nutrients":[{
            "name":"Vitamin B3","amount":0.01,"unit":"mg"},{"name":"Magnesium","amount":1.72,"unit":"mg"},
            {"name":"Zinc","amount":0.06,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},
            {"name":"Vitamin B6","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.01,"unit":"g"},{"name":"Manganese","amount":0.21,"unit":"mg"},
            {"name":"Vitamin C","amount":0.16,"unit":"mg"},{"name":"Net Carbohydrates","amount":0.3,"unit":"g"},
            {"name":"Saturated Fat","amount":0.01,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},
            {"name":"Fiber","amount":0.21,"unit":"g"},{"name":"Iron","amount":0.1,"unit":"mg"},{"name":"Phosphorus",
            "amount":1.34,"unit":"mg"},{"name":"Carbohydrates","amount":0.51,"unit":"g"},{"name":"Sodium",
            "amount":0.14,"unit":"mg"},{"name":"Calcium","amount":2.87,"unit":"mg"},{"name":"Potassium",
            "amount":8.39,"unit":"mg"},{"name":"Calories","amount":2.33,"unit":"kcal"},{"name":"Copper","amount":0.0,
            "unit":"mg"},{"name":"Protein","amount":0.08,"unit":"g"},{"name":"Fat","amount":0.05,"unit":"g"}]}],
            "caloricBreakdown":{"percentProtein":2.23,"percentFat":26.64,"percentCarbs":71.13},"weightPerServing":{
            "amount":143,"unit":"g"}},"summary":"Cardamon Infused Black Rice Pudding with Coconut Milk could be just 
            the <b>gluten free, dairy free, lacto ovo vegetarian, and fodmap friendly</b> recipe you've been looking 
            for. One serving contains <b>247 calories</b>, <b>1g of protein</b>, and <b>7g of fat</b>. For <b>87 
            cents per serving</b>, you get a dessert that serves 4. This recipe from Foodista has 1 fans. If you have 
            rice, salt, brown sugar, and a few other ingredients on hand, you can make it. From preparation to the 
            plate, this recipe takes roughly <b>roughly 45 minutes</b>. All things considered, we decided this recipe 
            <b>deserves a spoonacular score of 14%</b>. This score is rather bad. Similar recipes are <a 
            href=\"https://spoonacular.com/recipes/coconut-milk-rice-pudding-604699\">Coconut Milk Rice Pudding</a>, 
            <a href=\"https://spoonacular.com/recipes/rice-pudding-with-coconut-milk-309262\">Rice Pudding with 
            Coconut Milk</a>, and <a href=\"https://spoonacular.com/recipes/coconut-milk-risotto-arborio-rice-pudding
            -639794\">Coconut milk risotto (Arborio rice pudding)</a>.","cuisines":[],"dishTypes":["dessert"],
            "diets":["gluten free","dairy free","lacto ovo vegetarian","fodmap friendly","vegan"],"occasions":[],
            "analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Heat the oven to 300F.","ingredients":[],
            "equipment":[{"id":404784,"name":"oven","localizedName":"oven","image":"oven.jpg","temperature":{
            "number":300.0,"unit":"Fahrenheit"}}]},{"number":2,"step":"Put the rice in a food processor and pulse a 
            few times to break the grains up a bit and scratch their hulls; dont overdo it, or youll pulverize them. 
            This step is very very important.","ingredients":[{"id":0,"name":"grains","localizedName":"grains",
            "image":""},{"id":20444,"name":"rice","localizedName":"rice","image":"uncooked-white-rice.png"}],
            "equipment":[{"id":404771,"name":"food processor","localizedName":"food processor",
            "image":"food-processor.png"}]},{"number":3,"step":"Put all the ingredients in a 2-quart ovenproof pot or 
            Dutch oven. Stir a couple of times and put the pan in the oven, covered. Cook for 30 minutes, 
            then stir.","ingredients":[],"equipment":[{"id":404667,"name":"dutch oven","localizedName":"dutch oven",
            "image":"dutch-oven.jpg"},{"id":404784,"name":"oven","localizedName":"oven","image":"oven.jpg"},
            {"id":404645,"name":"frying pan","localizedName":"frying pan","image":"pan.png"}],"length":{"number":30,
            "unit":"minutes"}},{"number":4,"step":"Cook for 30 minutes more, and stir again. At this point the milk 
            will have darkened a bit and should be bubbling, and the rice will have begun to swell.","ingredients":[{
            "id":1077,"name":"milk","localizedName":"milk","image":"milk.png"},{"id":20444,"name":"rice",
            "localizedName":"rice","image":"uncooked-white-rice.png"}],"equipment":[],"length":{"number":30,
            "unit":"minutes"}},{"number":5,"step":"Cook for 30 minutes more. The milk will be even darker, 
            and the pudding will start to look more like rice than milk. Its almost done.","ingredients":[{"id":1077,
            "name":"milk","localizedName":"milk","image":"milk.png"},{"id":20444,"name":"rice",
            "localizedName":"rice","image":"uncooked-white-rice.png"}],"equipment":[],"length":{"number":30,
            "unit":"minutes"}},{"number":6,"step":"Return the mixture to the oven and check every 10 minutes, 
            stirring gently each time you check.","ingredients":[],"equipment":[{"id":404784,"name":"oven",
            "localizedName":"oven","image":"oven.jpg"}],"length":{"number":10,"unit":"minutes"}}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/cardamon-infused-black-rice-pudding-with-coconut-milk
            -637095","usedIngredientCount":1,"missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":99009,
            "amount":14.0,"unit":"ounce","unitLong":"ounces","unitShort":"oz","aisle":"Canned and Jarred",
            "name":"light coconut milk","original":"1 14-ounce cans light coconut milk","originalName":"light coconut 
            milk","meta":["light","canned"],"extendedName":"canned light coconut milk",
            "image":"https://spoonacular.com/cdn/ingredients_100x100/coconut-milk.jpg"},{"id":1002006,"amount":3.0,
            "unit":"sticks","unitLong":"sticks","unitShort":"sticks","aisle":"Spices and Seasonings","name":"cardamon pods","original":"A few cardamon pods, cinnamon sticks or saffron","originalName":"A few cardamon pods, 
            cinnamon or saffron","meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/cardamom.jpg"}],
            "usedIngredients":[{"id":10020036,"amount":0.3333333333333333,"unit":"cup","unitLong":"cups",
            "unitShort":"cup","aisle":"Pasta and Rice","name":"black rice","original":"1⁄3 cup long-grain black 
            rice","originalName":"long-grain black rice","meta":["long-grain","black"],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/black-rice.jpg"}],"unusedIngredients":[]},
            {"vegetarian":true,"vegan":true,"glutenFree":true,"dairyFree":true,"veryHealthy":false,"cheap":false,
            "veryPopular":false,"sustainable":false,"weightWatcherSmartPoints":13,"gaps":"no","lowFodmap":false,
            "aggregateLikes":1,"spoonacularScore":31.0,"healthScore":4.0,"creditsText":"swasthi",
            "license":"spoonacular's terms","sourceName":"spoonacular","pricePerServing":82.4,"extendedIngredients":[
            {"id":2019,"aisle":"Spices and Seasonings","image":"fenugreek.jpg","consistency":"solid",
            "name":"fenugreek seeds","nameClean":"fenugreek seeds","original":"1½ tsp fenugreek seeds/ 
            menthulu/methi","originalName":"fenugreek seeds/ menthulu/methi","amount":1.5,"unit":"tsp","meta":[],
            "measures":{"us":{"amount":1.5,"unitShort":"tsps","unitLong":"teaspoons"},"metric":{"amount":1.5,
            "unitShort":"tsps","unitLong":"teaspoons"}}},{"id":4582,"aisle":"Oil, Vinegar, Salad Dressing",
            "image":"vegetable-oil.jpg","consistency":"liquid","name":"oil","nameClean":"cooking oil","original":"oil 
            as needed","originalName":"oil as needed","amount":5.0,"unit":"servings","meta":["as needed"],
            "measures":{"us":{"amount":5.0,"unitShort":"servings","unitLong":"servings"},"metric":{"amount":5.0,
            "unitShort":"servings","unitLong":"servings"}}},{"id":20444,"aisle":"Pasta and Rice",
            "image":"uncooked-white-rice.png","consistency":"solid","name":"rice","nameClean":"rice","original":"2 
            cups dosa rice or ponni rice","originalName":"dosa rice or ponni rice","amount":2.0,"unit":"cups",
            "meta":[],"measures":{"us":{"amount":2.0,"unitShort":"cups","unitLong":"cups"},"metric":{
            "amount":473.176,"unitShort":"ml","unitLong":"milliliters"}}},{"id":2047,"aisle":"Spices and Seasonings",
            "image":"salt.jpg","consistency":"solid","name":"salt","nameClean":"table salt","original":"non iodised 
            salt as needed","originalName":"non iodised salt as needed","amount":5.0,"unit":"servings","meta":["as 
            needed"],"measures":{"us":{"amount":5.0,"unitShort":"servings","unitLong":"servings"},"metric":{
            "amount":5.0,"unitShort":"servings","unitLong":"servings"}}},{"id":93718,"aisle":"Pasta and Rice;Canned 
            and Jarred;Ethnic Foods","image":"urad-dal.png","consistency":"solid","name":"urad dal",
            "nameClean":"black lentils","original":"½ cup urad dal / minapa pappu","originalName":"urad dal / minapa 
            pappu","amount":0.5,"unit":"cup","meta":[],"measures":{"us":{"amount":0.5,"unitShort":"cups",
            "unitLong":"cups"},"metric":{"amount":118.294,"unitShort":"ml","unitLong":"milliliters"}}},{"id":null,
            "aisle":"?","image":null,"consistency":null,"name":"aval/ poha/ attukulu/avalakki","nameClean":null,
            "original":"1 cup medium aval/ poha/ attukulu/avalakki","originalName":"aval/ poha/ attukulu/avalakki",
            "amount":1.0,"unit":"cup","meta":[],"measures":{"us":{"amount":1.0,"unitShort":"cup","unitLong":"cup"},
            "metric":{"amount":236.588,"unitShort":"ml","unitLong":"milliliters"}}}],"id":624304,"title":"set dosa recipe","author":"swasthi","readyInMinutes":25,"servings":5,
            "sourceUrl":"https://spoonacular.com/-1419696663578",
            "image":"https://spoonacular.com/recipeImages/624304-312x231.jpg","imageType":"jpg","nutrition":{
            "nutrients":[{"name":"Calories","amount":458.25,"unit":"kcal","percentOfDailyNeeds":22.91},{"name":"Fat",
            "amount":14.72,"unit":"g","percentOfDailyNeeds":22.65},{"name":"Saturated Fat","amount":1.18,"unit":"g",
            "percentOfDailyNeeds":7.37},{"name":"Carbohydrates","amount":69.81,"unit":"g",
            "percentOfDailyNeeds":23.27},{"name":"Net Carbohydrates","amount":64.58,"unit":"g",
            "percentOfDailyNeeds":23.48},{"name":"Sugar","amount":0.09,"unit":"g","percentOfDailyNeeds":0.1},
            {"name":"Cholesterol","amount":0.0,"unit":"mg","percentOfDailyNeeds":0.0},{"name":"Sodium",
            "amount":199.43,"unit":"mg","percentOfDailyNeeds":8.67},{"name":"Protein","amount":10.33,"unit":"g",
            "percentOfDailyNeeds":20.66},{"name":"Manganese","amount":0.82,"unit":"mg","percentOfDailyNeeds":40.96},
            {"name":"Fiber","amount":5.24,"unit":"g","percentOfDailyNeeds":20.94},{"name":"Vitamin E","amount":2.53,
            "unit":"mg","percentOfDailyNeeds":16.88},{"name":"Selenium","amount":11.24,"unit":"µg",
            "percentOfDailyNeeds":16.06},{"name":"Iron","amount":2.48,"unit":"mg","percentOfDailyNeeds":13.77},
            {"name":"Vitamin K","amount":10.06,"unit":"µg","percentOfDailyNeeds":9.58},{"name":"Phosphorus",
            "amount":88.39,"unit":"mg","percentOfDailyNeeds":8.84},{"name":"Copper","amount":0.18,"unit":"mg",
            "percentOfDailyNeeds":8.76},{"name":"Vitamin B5","amount":0.75,"unit":"mg","percentOfDailyNeeds":7.5},
            {"name":"Vitamin B6","amount":0.13,"unit":"mg","percentOfDailyNeeds":6.4},{"name":"Vitamin B3",
            "amount":1.2,"unit":"mg","percentOfDailyNeeds":6.01},{"name":"Zinc","amount":0.83,"unit":"mg",
            "percentOfDailyNeeds":5.57},{"name":"Magnesium","amount":20.63,"unit":"mg","percentOfDailyNeeds":5.16},
            {"name":"Vitamin B1","amount":0.06,"unit":"mg","percentOfDailyNeeds":3.69},{"name":"Calcium",
            "amount":34.79,"unit":"mg","percentOfDailyNeeds":3.48},{"name":"Potassium","amount":93.69,"unit":"mg",
            "percentOfDailyNeeds":2.68},{"name":"Vitamin B2","amount":0.04,"unit":"mg","percentOfDailyNeeds":2.37},
            {"name":"Folate","amount":6.55,"unit":"µg","percentOfDailyNeeds":1.64},{"name":"Vitamin C","amount":0.87,
            "unit":"mg","percentOfDailyNeeds":1.06}],"properties":[{"name":"Glycemic Index","amount":12.24,
            "unit":""},{"name":"Glycemic Load","amount":35.61,"unit":""}],"flavonoids":[{"name":"Cyanidin",
            "amount":0.0,"unit":""},{"name":"Petunidin","amount":0.0,"unit":""},{"name":"Delphinidin","amount":0.0,
            "unit":""},{"name":"Malvidin","amount":0.0,"unit":""},{"name":"Pelargonidin","amount":0.0,"unit":""},
            {"name":"Peonidin","amount":0.0,"unit":""},{"name":"Catechin","amount":0.0,"unit":""},
            {"name":"Epigallocatechin","amount":0.0,"unit":""},{"name":"Epicatechin","amount":0.0,"unit":""},
            {"name":"Epicatechin 3-gallate","amount":0.0,"unit":""},{"name":"Epigallocatechin 3-gallate",
            "amount":0.0,"unit":""},{"name":"Theaflavin","amount":0.0,"unit":""},{"name":"Thearubigins","amount":0.0,
            "unit":""},{"name":"Eriodictyol","amount":0.0,"unit":""},{"name":"Hesperetin","amount":0.0,"unit":""},
            {"name":"Naringenin","amount":0.0,"unit":""},{"name":"Apigenin","amount":0.0,"unit":""},
            {"name":"Luteolin","amount":0.0,"unit":""},{"name":"Isorhamnetin","amount":0.0,"unit":""},
            {"name":"Kaempferol","amount":0.0,"unit":""},{"name":"Myricetin","amount":0.0,"unit":""},
            {"name":"Quercetin","amount":0.0,"unit":""},{"name":"Theaflavin-3,3'-digallate","amount":0.0,"unit":""},
            {"name":"Theaflavin-3'-gallate","amount":0.0,"unit":""},{"name":"Theaflavin-3-gallate","amount":0.0,
            "unit":""},{"name":"Gallocatechin","amount":0.0,"unit":""}],"ingredients":[{"id":2019,"name":"fenugreek 
            seeds","amount":0.3,"unit":"tsp","nutrients":[{"name":"Vitamin B3","amount":0.02,"unit":"mg"},
            {"name":"Folate","amount":0.63,"unit":"µg"},{"name":"Magnesium","amount":2.12,"unit":"mg"},
            {"name":"Zinc","amount":0.03,"unit":"mg"},{"name":"Vitamin B6","amount":0.01,"unit":"mg"},
            {"name":"Vitamin D","amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.0,"unit":"mg"},
            {"name":"Vitamin A","amount":0.67,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},
            {"name":"Cholesterol","amount":0.0,"unit":"mg"},{"name":"Manganese","amount":0.01,"unit":"mg"},
            {"name":"Vitamin C","amount":0.03,"unit":"mg"},{"name":"Selenium","amount":0.07,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":0.37,"unit":"g"},{"name":"Saturated Fat","amount":0.02,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.27,"unit":"g"},{"name":"Iron",
            "amount":0.37,"unit":"mg"},{"name":"Phosphorus","amount":3.29,"unit":"mg"},{"name":"Carbohydrates",
            "amount":0.65,"unit":"g"},{"name":"Sodium","amount":0.74,"unit":"mg"},{"name":"Calcium","amount":1.95,
            "unit":"mg"},{"name":"Potassium","amount":8.55,"unit":"mg"},{"name":"Calories","amount":3.59,
            "unit":"kcal"},{"name":"Copper","amount":0.01,"unit":"mg"},{"name":"Folic Acid","amount":0.0,
            "unit":"µg"},{"name":"Protein","amount":0.26,"unit":"g"},{"name":"Fat","amount":0.07,"unit":"g"}]},
            {"id":4582,"name":"oil","amount":1.0,"unit":"servings","nutrients":[{"name":"Vitamin B3","amount":0.0,
            "unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.0,"unit":"g"},
            {"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},{"name":"Poly 
            Unsaturated Fat","amount":3.93,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},
            {"name":"Vitamin E","amount":2.45,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":8.86,"unit":"g"},{"name":"Manganese","amount":0.0,"unit":"mg"},
            {"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Trans Fat","amount":0.06,"unit":"g"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.0,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K","amount":9.98,"unit":"µg"},
            {"name":"Saturated Fat","amount":1.03,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.0,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,
            "unit":"mg"},{"name":"Carbohydrates","amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,
            "unit":"µg"},{"name":"Sodium","amount":0.0,"unit":"mg"},{"name":"Calcium","amount":0.0,"unit":"mg"},
            {"name":"Potassium","amount":0.0,"unit":"mg"},{"name":"Choline","amount":0.03,"unit":"mg"},
            {"name":"Calories","amount":123.76,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat",
            "amount":14.0,"unit":"g"}]},{"id":20444,"name":"rice","amount":0.4,"unit":"cups","nutrients":[{
            "name":"Vitamin B3","amount":1.18,"unit":"mg"},{"name":"Folate","amount":5.92,"unit":"µg"},
            {"name":"Sugar","amount":0.09,"unit":"g"},{"name":"Magnesium","amount":18.5,"unit":"mg"},{"name":"Zinc",
            "amount":0.81,"unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.13,"unit":"g"},{"name":"Vitamin B6",
            "amount":0.12,"unit":"mg"},{"name":"Vitamin E","amount":0.08,"unit":"mg"},{"name":"Vitamin D",
            "amount":0.0,"unit":"µg"},{"name":"Vitamin B1","amount":0.05,"unit":"mg"},{"name":"Vitamin A",
            "amount":0.0,"unit":"IU"},{"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol",
            "amount":0.0,"unit":"mg"},{"name":"Mono Unsaturated Fat","amount":0.15,"unit":"g"},{"name":"Manganese",
            "amount":0.81,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},{"name":"Selenium",
            "amount":11.17,"unit":"µg"},{"name":"Net Carbohydrates","amount":58.2,"unit":"g"},{"name":"Vitamin B5",
            "amount":0.75,"unit":"mg"},{"name":"Vitamin K","amount":0.07,"unit":"µg"},{"name":"Saturated Fat",
            "amount":0.13,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.04,
            "unit":"mg"},{"name":"Fiber","amount":0.96,"unit":"g"},{"name":"Iron","amount":0.59,"unit":"mg"},
            {"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":85.1,"unit":"mg"},
            {"name":"Carbohydrates","amount":59.16,"unit":"g"},{"name":"Lycopene","amount":0.0,"unit":"µg"},
            {"name":"Sodium","amount":3.7,"unit":"mg"},{"name":"Calcium","amount":20.72,"unit":"mg"},
            {"name":"Potassium","amount":85.1,"unit":"mg"},{"name":"Choline","amount":4.29,"unit":"mg"},
            {"name":"Calories","amount":270.1,"unit":"kcal"},{"name":"Copper","amount":0.16,"unit":"mg"},
            {"name":"Folic Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":5.28,"unit":"g"},{"name":"Fat",
            "amount":0.49,"unit":"g"}]},{"id":2047,"name":"salt","amount":1.0,"unit":"servings","nutrients":[{
            "name":"Vitamin B3","amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar",
            "amount":0.0,"unit":"g"},{"name":"Magnesium","amount":0.01,"unit":"mg"},{"name":"Zinc","amount":0.0,
            "unit":"mg"},{"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,
            "unit":"mg"},{"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":0.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.01,"unit":"mg"},
            {"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.0,"unit":"mg"},
            {"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net Carbohydrates","amount":0.0,"unit":"g"},
            {"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin K","amount":0.0,"unit":"µg"},
            {"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol","amount":0.0,"unit":"g"},
            {"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":0.0,"unit":"g"},{"name":"Iron",
            "amount":0.0,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},{"name":"Phosphorus","amount":0.0,
            "unit":"mg"},{"name":"Carbohydrates","amount":0.0,"unit":"g"},{"name":"Lycopene","amount":0.0,
            "unit":"µg"},{"name":"Sodium","amount":193.79,"unit":"mg"},{"name":"Calcium","amount":0.12,"unit":"mg"},
            {"name":"Potassium","amount":0.04,"unit":"mg"},{"name":"Choline","amount":0.0,"unit":"mg"},
            {"name":"Calories","amount":0.0,"unit":"kcal"},{"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Folic 
            Acid","amount":0.0,"unit":"µg"},{"name":"Protein","amount":0.0,"unit":"g"},{"name":"Fat","amount":0.0,
            "unit":"g"}]},{"id":93718,"name":"urad dal","amount":0.1,"unit":"cup","nutrients":[{"name":"Vitamin B3",
            "amount":0.0,"unit":"mg"},{"name":"Folate","amount":0.0,"unit":"µg"},{"name":"Sugar","amount":0.0,
            "unit":"g"},{"name":"Magnesium","amount":0.0,"unit":"mg"},{"name":"Zinc","amount":0.0,"unit":"mg"},
            {"name":"Poly Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Vitamin B6","amount":0.0,"unit":"mg"},
            {"name":"Vitamin E","amount":0.0,"unit":"mg"},{"name":"Vitamin D","amount":0.0,"unit":"µg"},
            {"name":"Vitamin B1","amount":0.0,"unit":"mg"},{"name":"Vitamin A","amount":1.0,"unit":"IU"},
            {"name":"Vitamin B12","amount":0.0,"unit":"µg"},{"name":"Cholesterol","amount":0.0,"unit":"mg"},
            {"name":"Mono Unsaturated Fat","amount":0.0,"unit":"g"},{"name":"Fluoride","amount":0.0,"unit":"mg"},
            {"name":"Manganese","amount":0.0,"unit":"mg"},{"name":"Vitamin C","amount":0.84,"unit":"mg"},
            {"name":"Trans Fat","amount":0.0,"unit":"g"},{"name":"Selenium","amount":0.0,"unit":"µg"},{"name":"Net 
            Carbohydrates","amount":6.0,"unit":"g"},{"name":"Vitamin B5","amount":0.0,"unit":"mg"},{"name":"Vitamin 
            K","amount":0.0,"unit":"µg"},{"name":"Saturated Fat","amount":0.0,"unit":"g"},{"name":"Alcohol",
            "amount":0.0,"unit":"g"},{"name":"Vitamin B2","amount":0.0,"unit":"mg"},{"name":"Fiber","amount":4.0,
            "unit":"g"},{"name":"Iron","amount":1.51,"unit":"mg"},{"name":"Caffeine","amount":0.0,"unit":"mg"},
            {"name":"Phosphorus","amount":0.0,"unit":"mg"},{"name":"Carbohydrates","amount":10.0,"unit":"g"},
            {"name":"Sodium","amount":1.2,"unit":"mg"},{"name":"Calcium","amount":12.0,"unit":"mg"},
            {"name":"Potassium","amount":0.0,"unit":"mg"},{"name":"Calories","amount":60.8,"unit":"kcal"},
            {"name":"Copper","amount":0.0,"unit":"mg"},{"name":"Protein","amount":4.8,"unit":"g"},{"name":"Fat",
            "amount":0.16,"unit":"g"}]}],"caloricBreakdown":{"percentProtein":9.12,"percentFat":29.24,
            "percentCarbs":61.64},"weightPerServing":{"amount":110,"unit":"g"}},"summary":"You can never have too 
            many side dish recipes, so give set dosa  a try. For <b>82 cents per serving</b>, this recipe <b>covers 
            8%</b> of your daily requirements of vitamins and minerals. One serving contains <b>458 calories</b>, 
            <b>10g of protein</b>, and <b>15g of fat</b>. If you have aval/ poha/ attukulu/avalakki, non iodised 
            salt, oil, and a few other ingredients on hand, you can make it. From preparation to the plate, 
            this recipe takes around <b>25 minutes</b>. It is a good option if you're following a <b>gluten free and 
            vegan</b> diet. Try <a href=\"https://spoonacular.com/recipes/godhuma-dosa-instant-wheat-dosa-south
            -indian-breakfast-s-564757\">Godhuma Dosa – Instant Wheat Dosa | South Indian Breakfast s</a>, 
            <a href=\"https://spoonacular.com/recipes/sabudana-dosa-sago-dosa-for-fast-vrat-616225\">Sabudana dosa | 
            Sago dosa for fast, vrat</a>, and <a 
            href=\"https://spoonacular.com/recipes/poha-dosa-or-atukula-dosa-how-to-make-poha-dosa-487542\">poha 
            dosan or atukula dosa , how to make poha dosa</a> for similar recipes.","cuisines":[],"dishTypes":["side 
            dish"],"diets":["gluten free","dairy free","lacto ovo vegetarian","vegan"],"occasions":[],
            "analyzedInstructions":[{"name":"","steps":[{"number":1,"step":"Check set dosa recipe instructions",
            "ingredients":[],"equipment":[]}]}],
            "spoonacularSourceUrl":"https://spoonacular.com/set-dosa-recipe-624304","usedIngredientCount":1,
            "missedIngredientCount":2,"likes":0,"missedIngredients":[{"id":2019,"amount":1.5,"unit":"tsp",
            "unitLong":"teaspoons","unitShort":"tsp","aisle":"Spices and Seasonings","name":"fenugreek seeds",
            "original":"1½ tsp fenugreek seeds/ menthulu/methi","originalName":"fenugreek seeds/ menthulu/methi",
            "meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/fenugreek.jpg"},{"id":93718,
            "amount":0.5,"unit":"cup","unitLong":"cups","unitShort":"cup","aisle":"Pasta and Rice;Canned and 
            Jarred;Ethnic Foods","name":"urad dal","original":"½ cup urad dal / minapa pappu","originalName":"urad 
            dal / minapa pappu","meta":[],"image":"https://spoonacular.com/cdn/ingredients_100x100/urad-dal.png"}],
            "usedIngredients":[{"id":20444,"amount":2.0,"unit":"cups","unitLong":"cups","unitShort":"cup",
            "aisle":"Pasta and Rice","name":"rice","original":"2 cups dosa rice or ponni rice","originalName":"dosa rice or ponni rice","meta":[],
            "image":"https://spoonacular.com/cdn/ingredients_100x100/uncooked-white-rice.png"}],"unusedIngredients":[
            ]}],"offset":0,"number":5,"totalResults":214}''')
        ]
        expected_results = [
            r'''[{"name": "Simple Spinach and Tomato Frittata", "img_url": "https://spoonacular.com/recipeImages/769775-312x231.jpg", "used_ingr": ["cherry tomatoes"], "missed_ingr": ["burger skillet", "eggs", "spinach leaves"], "carbs": [7.32, "g"], "proteins": [12.62, "g"], "calories": [156.15, "kcal"]}, {"name": "Jalapeno Queso With Goat Cheese", "img_url": "https://spoonacular.com/recipeImages/648368-312x231.jpg", "used_ingr": ["canned tomatoes"], "missed_ingr": ["goat cheese", "jalapeno pepper", "hot sauce"], "carbs": [17.58, "g"], "proteins": [31.71, "g"], "calories": [474.18, "kcal"]}, {"name": "Eggplant pizzette", "img_url": "https://spoonacular.com/recipeImages/642303-312x231.jpg", "used_ingr": ["tomatoes"], "missed_ingr": ["eggplant", "swiss cheese", "basil leaves"], "carbs": [11.38, "g"], "proteins": [10.93, "g"], "calories": [178.07, "kcal"]}, {"name": "Green Tomato Salad", "img_url": "https://spoonacular.com/recipeImages/645555-312x231.jpg", "used_ingr": ["green tomato"], "missed_ingr": ["sumac", "mint leaves"], "carbs": [9.88, "g"], "proteins": [2.33, "g"], "calories": [168.42, "kcal"]}, {"name": "Easy Tomato Soup", "img_url": "https://spoonacular.com/recipeImages/1674265-312x231.jpg", "used_ingr": ["tomatoes"], "missed_ingr": ["butter", "onion", "vegetable broth"], "carbs": [23.29, "g"], "proteins": [3.94, "g"], "calories": [299.04, "kcal"]}]''',
            r'''[{"name": "Chestnuts Roasting on an Open Fire", "img_url": "https://spoonacular.com/recipeImages/1697797-312x231.jpg", "used_ingr": ["chestnut is japan's most ancient fruit. kuri was cultivated even before growing rice"], "missed_ingr": ["all the nuts", "in hungarian cuisine"], "carbs": [2.66, "g"], "proteins": [0.26, "g"], "calories": [12.35, "kcal"]}, {"name": "Cardamon Infused Black Rice Pudding with Coconut Milk", "img_url": "https://spoonacular.com/recipeImages/637095-312x231.jpg", "used_ingr": ["black rice"], "missed_ingr": ["light coconut milk", "cardamon pods"], "carbs": [42.7, "g"], "proteins": [1.34, "g"], "calories": [246.56, "kcal"]}, {"name": "set dosa recipe", "img_url": "https://spoonacular.com/recipeImages/624304-312x231.jpg", "used_ingr": ["rice"], "missed_ingr": ["fenugreek seeds", "urad dal"], "carbs": [69.81, "g"], "proteins": [10.33, "g"], "calories": [458.25, "kcal"]}, {"name": "Nasi Pudina (Mint Rice)", "img_url": "https://spoonacular.com/recipeImages/652965-312x231.jpg", "used_ingr": ["rice"], "missed_ingr": ["mint leaves", "coconut milk"], "carbs": [77.22, "g"], "proteins": [8.16, "g"], "calories": [456.81, "kcal"]}, {"name": "Kappa Maki", "img_url": "https://spoonacular.com/recipeImages/648742-312x231.jpg", "used_ingr": ["sushi rice"], "missed_ingr": ["cucumber", "nori"], "carbs": [77.24, "g"], "proteins": [6.82, "g"], "calories": [351.69, "kcal"]}]'''
        ]

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
