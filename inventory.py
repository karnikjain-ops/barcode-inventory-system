import json
import os

with open("inventory.json","r") as f:
    inventory = json.load(f)

def add_item(code):
    if code in inventory:
        inventory[code]["quantity"] = int(inventory[code]["quantity"]) + 1
        print (inventory[code]["quantity"])
        with open("inventory.json","w") as f:
            json.dump(inventory,f,indent=4)