

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