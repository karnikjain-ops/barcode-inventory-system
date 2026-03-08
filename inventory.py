import json
import os

with open("inventory.json","r") as f:
    inventory = json.load(f)

def add_item(code):
    if code in inventory:
        inventory[code]["quantity"] = int(inventory[code]["quantity"]) + 1
        print("new quantity after add/buy")
        print (inventory[code]["quantity"])
        with open("inventory.json","w") as f:
            json.dump(inventory,f,indent=4)

    if code not in inventory:
        inventory[code] = {
            "name" : input("What is the name?"),
            "quantity" : int(input("What is the quantity?")),
            "price" : int(input("What is the price?")),
        }


def remove_items(code):
    if code in inventory:
        inventory[code]["quantity"] = int(inventory[code]["quantity"]) - 1
        print("quantity left after sell/remove")
        print(inventory[code]["quantity"])
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)

    if code not in inventory:
        print("No items found")





def give_details(code):
    if code in inventory:
        print(inventory[code])


    if code not in inventory:
        print("No items found")