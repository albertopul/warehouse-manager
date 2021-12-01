# warehouse_manager.py
# =======================
# This is a warehouse management program for a cycling store.

#imports
import sys
import csv
from tabulate import tabulate
import collections

# List of items in store:
items = [
    {"Name": "Frame", "Quantity": 34, "Unit": "pcs", "Unit Price (PLN)": 2000},
    {"Name": "Handlebar", "Quantity": 24, "Unit": "pcs", "Unit Price (PLN)": 701},
    {"Name": "Stem", "Quantity": 55, "Unit": "pcs", "Unit Price (PLN)": 321},
    {"Name": "Derailleur", "Quantity": 13, "Unit": "pcs", "Unit Price (PLN)": 699},
    {"Name": "Crankset", "Quantity": 42, "Unit": "pcs", "Unit Price (PLN)": 574},
    {"Name": "Tire", "Quantity": 66, "Unit": "pcs", "Unit Price (PLN)": 212},]


sold_items = []

costs_list = []

income_list = [] 

csv_columns = ["Name", "Quantity", "Unit", "Unit Price (PLN)"]

# Definitions:

def get_items():
    header = items[0].keys()
    rows = [x.values() for x in items]
    print(tabulate(rows, header))


def add_item():
    print("Adding to warehouse...")
    exist = False
    name = input("Name: ")
    for obj in items:
        if obj["Name"] == name:
            quantity = int(input("Quantity: "))
            obj["Quantity"] += quantity
            print("Successfully added to warehouse. Current status:")
            get_items()
            exist = True
    if exist == False:
        quantity = int(input("Quantity: "))
        unit = input("Unit: ")
        unit_price = int(input("Price: "))
        print("Successfully added to warehouse. Current status:")
        items.append({"Name" : name, "Quantity" : quantity, "Unit" : unit, "Unit Price (PLN)" : unit_price})
        get_items()
    


def sell_item():
    print("Selling from warehouse...")
    exist = False
    name = input("Name: ")
    for obj in items:
        if obj["Name"] == name:
            quantity = int(input("Quantity: "))
            if quantity <= obj["Quantity"]:
                obj["Quantity"] -= quantity
                unit = obj["Unit"]
                unit_price = obj["Unit Price (PLN)"]
                print(f"Successfully sold {quantity} {unit} of {name}. Current status:")
                sold_items.append({"Name" : name, "Quantity" : quantity, "Unit" : unit, "Unit Price (PLN)" : unit_price})
                get_items()
                exist = True
                break
            if quantity > obj["Quantity"]:
                print("We don't have so much of it... :(")
                get_items()
                exist = True
                break
            elif exist == False:
                print("Product doesn't exist in warehouse!")
                break


def get_costs():
    for item in items:
        costs = item.get("Quantity") * item.get("Unit Price (PLN)")
        costs_list.append(costs)     
    costs_list_sum = sum(costs_list)
    print(f"Costs: {costs_list_sum}")
    return costs_list_sum  



def get_income():
    for item in sold_items:
        income = item.get("Quantity") * item.get("Unit Price (PLN)")
        income_list.append(income)
    income_list_sum = sum(income_list)
    print(f"Income: {income_list_sum}")
    return income_list_sum

def show_revenue():
    print("Revenue brakdown (PLN)")
    costs = get_costs()
    income = get_income()
    revenue = income - costs
    print("-------------------")
    print(f"Revenue: {revenue}")



def export_items_to_csv(items):
    try:
        with open("warehouse.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in items:
                writer.writerow(item)
    except IOError:
        print("I/O error")

def export_sales_to_csv(sold_items):
    try:
        with open("record.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in sold_items:
                writer.writerow(item)
    except IOError:
        print("I/O error")

def load_items_from_csv(items):
    try:
        with open("warehouse.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(row)      
            return items  
    except IOError as err:
            print("I/O error({0})".format(err))    

def load_sold_items_from_csv(sold_items):
    try:
        with open("record.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sold_items.append(row) 
            return sold_items
    except IOError as err:
            print("I/O error({0})".format(err))

    

while(True):

    hello = input("What would you like to do? (show, add, sell, show revenue, save, load, exit) ")
    if hello == "show":
        get_items()
    elif hello == "add":
        add_item()
    elif hello == "sell":
        sell_item()
    elif hello == "show revenue":
        show_revenue()
    elif hello == "save":
        export_items_to_csv(items)
        export_sales_to_csv(sold_items)
        print(f"Sucessfully saved data to warehouse.csv")
        print(f"Sucessfully saved data to record.csv")
    elif hello == "load":
        sold_items.clear()
        items.clear()
        load_items_from_csv(items)
        load_sold_items_from_csv(sold_items)
        print(sys.argv)
        print(f"Sucessfully loaded data from warehouse.csv")
        print(f"Sucessfully loaded data from record.csv")
    elif hello == "exit":
        sys.exit("Exiting... Bye!")