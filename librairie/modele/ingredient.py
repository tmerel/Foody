from nutrition import Nutrition
import uuid

class Ingredient(object):
    def __init__(self,name:str="",type:int=0,nutr:Nutrition=None):
        self.uid = uuid.uuid5()
        self.name = name
        self.type = type
        self.nutrition = nutr
    

    @staticmethod
    def From_json(db:dict):
        ingredient = Ingredient()
        ingredient.uid = db["uid"]
        ingredient.name = db["name"]
        ingredient.type = db["type"]
        ingredient.nutrition = Nutrition.From_json(db["nutrition"])
        return ingredient

