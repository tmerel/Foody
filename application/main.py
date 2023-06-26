#! /usr/bin/env python3

import sys

sys.path.append(".")
sys.path.append("..")
from librairie.modele.ingredient import Ingredient,IngredientEncoder,IngredientDecoder
from librairie.modele.nutrition import Nutrition
import json
        

Ing= []



with open("database.json","r") as template :
    json_object= json.loads(template.read())
    
    Ing= IngredientDecoder.decode_json(json_object)

print(Ing)