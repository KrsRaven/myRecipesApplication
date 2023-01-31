from urllib import request, parse
import json
from objects import Area, Category, Ingredient, Meal, Instruction, Measure


def get_categories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = request.urlopen(url)
    categories = []

    # API access
    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data ['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None
    
    return categories


def get_meal_byCategories(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data ['meals']:
            meal = Meal(meal_data['strMeal'])
            meals.append(meal)

    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None
    
    return meals


def get_instruction_byName(link, meal_name):
    # add link as a variable, so the function can be used 
    # for both Meal by Name and Random Meal modules
    url = link + parse.quote(meal_name)
    f = request.urlopen(url)

    while True:
        try:
            data = json.loads(f.read().decode('utf-8'))
            if data ['meals'] is None:
                break
            else:
                for instruction_data in data ['meals']:
                    instruction = Instruction(instruction_data['strInstructions'])
                
        except(ValueError, KeyError, TypeError):
            print("JSON format error")
            return None
    
        return instruction


def get_measures_byName(link, meal_name):
    # add link as a variable, so the function can be used 
    # for both Meal by Name and Random Meal modules
    url = link + parse.quote(meal_name)
    f = request.urlopen(url)
    measures = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for measure_data in data ['meals']:
            for key in list(measure_data.keys()):
                # add all measures to the list, remove empty items
                if "strMeasure" in key and measure_data[key] != "":
                    measure = Measure(measure_data[key])
                    measures.append(measure)
            
    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None
    
    return measures


def get_ingredients_byName(link, meal_name):
    # add link as a variable, so the function can be used 
    # for both Meal by Name and Random Meal modules
    url = link + parse.quote(meal_name)
    f = request.urlopen(url)
    ingredients = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for ingredient_data in data ['meals']:
            for key in list(ingredient_data.keys()):
                # add all ingredients to the list
                if "strIngredient" in key and ingredient_data[key] != "":
                    ingredient = Ingredient(ingredient_data[key])
                    ingredients.append(ingredient)
            
    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None

    return ingredients


def get_mealName():
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = request.urlopen(url)

    try:
        data = json.loads(f.read().decode('utf-8'))
        for name_data in data ['meals']:
            name = Meal(name_data['strMeal'])
            
    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None

    return name.get_meal_name()


def get_areas():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data ['meals']:
            area = Area(area_data['strArea'])
            areas.append(area)

    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None
    
    return areas


def get_meal_byAreas(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data ['meals']:
            meal = Meal(meal_data['strMeal'])
            meals.append(meal)

    except(ValueError, KeyError, TypeError):
        print("JSON format error")
        return None
    
    return meals