import json

class Nutrition (object):
    def __init__(self,cal:int=0,glu:float=0.0,lip:float=0.0,prot:float=0.0) -> None:
        self.calory = cal
        self.glucide = glu
        self.lipid = lip
        self.protein = prot

    @staticmethod
    def From_json(db:dict):
        nutrition = Nutrition()
        nutrition.calory = db["calory"]
        nutrition.glucide = db["glucide"]
        nutrition.lipid = db["lipid"]
        nutrition.protein = db["protein"]
        return nutrition

    def To_json(self):
        return {"calory":self.calory, "glucide": self.glucide, "lipid": self.lipid, "protein": self.protein}


class NutritionEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Nutrition):
            return obj.To_json()
        return json.JSONEncoder.default(self,obj)

class NutritionDecoder(object):

    @staticmethod
    def decode_json(obj):
        if isinstance(obj,list):
            nutr = []
            for l in obj :
                nutr.append(Nutrition.From_json(l))
            return nutr
        else :
            return Nutrition.From_json(obj)