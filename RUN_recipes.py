#! /usr/bin/usr python3
import textwrap
import requests

def show_title():
    print("The Recipes Program")
    print()


def show_menu():
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("7 - Menu")
    print("0 - Exit the program")
    print()


# COMMAND 1 - List all Categories
def list_categories():
    categories = requests.get_categories()

    if categories is None:
        print("Technical difficulties. Please try again later.")
    else:
        print()
        print("CATEGORIES")

    for i in range (len(categories)):
        category = categories[i]
        print("  " + category.get_name())
    print()


# function for listing filtered meals
def list_meals(filter, meals):
    if meals is None:
        print("Technical difficulties. Please try again later.")
    else:
        print(filter.upper(), "MEALS")
        for i in range (len(meals)):
            meal = meals[i]
            print("  " + meal.get_meal_name())
        print()


# COMMAND 2 - List all Meals for Categories
def list_meals_for_category():
    decide_category = input("Enter a Category: ")

    categories = requests.get_categories()
    found = False

    if categories is None:
        print("Technical difficulties. Please try again later.")
    else:
        for i in range(len(categories)):
            category = categories[i]
            # check the whole list for the category entered
            if decide_category.lower() == category.get_name().lower():
                found = True
                break
    
        if found == True:
            meals = requests.get_meal_byCategories(decide_category)
            print()
            list_meals(decide_category, meals)
        else:
            print("Invalid category. Please try again.")
            print()


# COMMAND 3 - Search Meals by Name
def list_recipe_by_mealName():
    while True:
        meal = input("Enter Meal Name: ")

        if meal is None:
            print("Technical difficulties. Please try again later.")
        else:
            instruction = requests.get_instruction_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal)
            # check if meal name valid, if not, show the error message
            if instruction is None:
                print("Invalid meal name. Please try again.")
                print()
                break
            else:
                print()
                # print the meal name
                print("Recipe: ", meal)
                print()

                # format and print the title and instruction
                print("Instructions:")
                my_wrap = textwrap.TextWrapper(width=80)
                wrap_list = my_wrap.wrap(instruction.get_instruction())
                for line in wrap_list:
                    print(line)
                print()

                # format and print titles and lists into two columns
                print("{:<30}{:<10}".format("Measure", "Ingredient"))
                print("-" * 60)
                measures = requests.get_measures_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal)
                ingredients = requests.get_ingredients_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal)
                for m, i in zip(measures, ingredients):  # use the built-in function zip() to aggregate lists
                    print("{:<30}{:<10}".format(m.get_measures(), i.get_ingredients()))
                print()
                break


# COMMAND 4 - Random Meal
def random_meal():
    meal_name = requests.get_mealName()

    print("A random meal was selected just for you!")
    print()
    # print the name of the random meal
    print("Recipe: ", meal_name)
    print()

    # format and print the title and instruction
    print("Instructions:")
    instruction = requests.get_instruction_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal_name)
    my_wrap = textwrap.TextWrapper(width=80)
    wrap_list = my_wrap.wrap(instruction.get_instruction())
    for line in wrap_list:
        print(line)
    print()

    # format and print titles and lists into two columns
    print("{:<30}{:<10}".format("Measure", "Ingredient"))
    print("-" * 60)
    measures = requests.get_measures_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal_name)
    ingredients = requests.get_ingredients_byName("https://www.themealdb.com/api/json/v1/1/search.php?s=", meal_name)
    for m, i in zip(measures, ingredients):  # use the built-in function zip() to aggregate
        print("{:<30}{:<10}".format(m.get_measures(), i.get_ingredients()))
    print()


# COMMAND 5 - List all Areas
def list_areas():
    areas = requests.get_areas()

    if areas is None:
        print("Technical difficulties. Please try again later.")
    else:
        print()
        print("AREAS: ")

    for i in range (len(areas)):
        area = areas[i]
        print("  " + area.get_areas())
    print()


# COMMAND 6 - Search Meals by Area
def list_meals_for_area():
    decide_area = input("Enter an Area: ")

    areas = requests.get_areas()
    found = False

    if areas is None:
        print("Technical difficulties. Please try again later.")
    else:
        for i in range(len(areas)):
            area = areas[i]
            if decide_area.lower() == area.get_areas().lower():
                found = True
                break

        if found == True:
            meals = requests.get_meal_byAreas(decide_area)
            print()
            list_meals(decide_area, meals)
        else:
            print("Invalid area. Please try again.")
            print()




def main():
    show_title()
    show_menu()

    while True:
        command = input("Command: ")
        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_for_category()
        elif command == "3":
            list_recipe_by_mealName()
        elif command == "4":
            random_meal()
        elif command == "5":
            list_areas()
        elif command == "6":
            list_meals_for_area()
        elif command == "7":
            print()
            show_menu()
        elif command == "0":
            print()
            print("Thank you for dining with us!")
            break
        else:
            print("Not a valid command. Please try again.")
            print()



if __name__ == "__main__":
    main()