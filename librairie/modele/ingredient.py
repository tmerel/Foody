from librairie.modele.nutrition import Nutrition
import uuid
import json

class Ingredient(object):
    def __init__(self,name:str="",type:int=0,nutr:Nutrition=None):
        self.uid = str(uuid.uuid1())
        self.name = name
        self.type = type
        self.nutrition = nutr
    

    @staticmethod
    def From_json(db:dict):
        ingredient = Ingredient()
        print(db)
        ingredient.uid = db["uid"]
        ingredient.name = db["name"]
        ingredient.type = db["type"]
        ingredient.nutrition = Nutrition.From_json(db["nutrition"])
        return ingredient

    def To_json(self):
        return {"uid":self.uid,"name":self.name, "type":self.type,"nutrition":self.nutrition.To_json()}


class IngredientEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Ingredient):
            return obj.To_json()
        return json.JSONEncoder.default(self,obj)


class IngredientDecoder(object):

    @staticmethod
    def decode_json(obj):
        if isinstance(obj,list):
            ing = []
            for l in obj :
                ing.append(Ingredient.From_json(l))
            return ing
        else :
            return Ingredient.From_json(obj)
