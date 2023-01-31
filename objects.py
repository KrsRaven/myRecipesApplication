class Category:
    def __init__(self, category):
        self.__category = category

    def get_name(self):
        return self.__category


class Meal:
    def __init__(self, meal_name):
        self.__meal_name = meal_name
        
    def get_meal_name(self):
        return self.__meal_name


class Instruction:
    def __init__(self, instruction):
        self.__instruction = instruction
    
    def get_instruction(self):
        return self.__instruction


class Measure:
    def __init__(self, measure):
        self.__measure = measure

    def get_measures(self):
        return self.__measure


class Ingredient:
    def __init__(self, ingredient):
        self.__ingredient = ingredient

    def get_ingredients(self):
        return self.__ingredient


class Area:
    def __init__(self, area):
        self.__area = area

    def get_areas(self):
        return self.__area