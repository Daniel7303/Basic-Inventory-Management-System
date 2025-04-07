# from tabulate import tabulate

import json
import os


def cart():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    return {"name": name, "price": price, "quantity": quantity}


INVENTORY_FILE = "inventory.json"


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f)


def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    return []


inventory_list = load_inventory()
while True:
    store_manager = input(" Enter A to add or R to remove or Q to quit: ").upper()

    if store_manager == "A":
        item = cart()
        if any(i["name"].lower() == item["name"].lower() for i in inventory_list):
            print("item already in cart")
            continue
        else:
            inventory_list.append(item)
            save_inventory(inventory_list)
            print(f"{item['name']} added to cart")
    elif store_manager == "R":
        print("Which item would you like to remove?: ")
        remove_item = input("item: ")
        found = False
        for item in inventory_list:
            if item["name"].lower() == remove_item.lower():
                inventory_list.remove(item)
                save_inventory(inventory_list)
                print(f"{remove_item} was removed from cart")

                found = True
                break
        if not found:
            print("Item not in cart")
    elif store_manager == "Q":
        if inventory_list:
            headers = inventory_list[0].keys()
            print("\n Cart summary")
            print("{:<10} {:<10} {:<10}".format(*headers).capitalize() + "Value")
            total_value = 0
            print("-" * 50)
            for item in inventory_list:
                # print("{:<10} {:<10} {:<10}".format(*item.values()))
                value = item["quantity"] * item["price"]
                total_value += value
                print("{:<10} ₦{:<9.2f} {:<10} ₦{:<10.2f}".format(
                    item["name"], item["price"], item["quantity"], value
                ))

            print("-" * 50)
            print(f"\n Total in Inventory ₦{total_value} ")
        else:
            print("Cart is empty")
        break
