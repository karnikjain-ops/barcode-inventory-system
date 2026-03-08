from scanner import scanner
from inventory import add_item
from inventory import remove_items
from inventory import give_details



print("Welcome to the Inventory")
print("What would you like to do?")
do=input()
match do :
    case "add" | "sell":
        code = scanner()
        add_item(code)
    case "remove" | "sell":
        code = scanner()
        remove_items(code)
    case "detailing":
        code = scanner()
        give_details(code)

