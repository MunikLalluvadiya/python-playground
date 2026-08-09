import csv
from FoodItem import FoodItem


class Cart:

    def __init__(self):
        self.List_Of_SelectedItems = [] 
        self.Total_Price = 0.0

    def Add_Item(self):
        restaurant_id = input(" Enter Restaurant ID : ")
        food_id = input(" Enter Food ID : ")
        quantity = int(input(" Enter Quantity : "))

        found_item = None
        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row and row[0] == restaurant_id:
                    items_str = row[4]
                    if items_str:
                        for item_str in items_str.split(";"):
                            fid, fname, category, price, availability = item_str.split(":")
                            if fid == food_id:
                                found_item = FoodItem(fid, fname, category, float(price), availability == "True")
                    break

        if found_item is None:
            print(" Deta NotFound! ")
            return

        self.List_Of_SelectedItems.append({"item": found_item, "quantity": quantity})
        self.Calculate_Total()
        print(f" Added {quantity} x {found_item.Food_Name} to cart.")

    def Remove_Item(self):
        food_id = input(" Enter Food ID to remove : ")
        for entry in self.List_Of_SelectedItems:
            if entry["item"].Food_ID == food_id:
                self.List_Of_SelectedItems.remove(entry)
                self.Calculate_Total()
                print(f" Removed {food_id} from cart.")
                return
        print(" Deta NotFound! ")

    def Update_Quantity(self):
        food_id = input(" Enter Food ID to update quantity : ")
        for entry in self.List_Of_SelectedItems:
            if entry["item"].Food_ID == food_id:
                new_quantity = int(input(" Enter New Quantity : "))
                entry["quantity"] = new_quantity
                self.Calculate_Total()
                print(" Quantity Updated.")
                return
        print(" Deta NotFound! ")

    def View_Cart(self):
        if not self.List_Of_SelectedItems:
            print(" Cart is empty.")
            return
        for entry in self.List_Of_SelectedItems:
            item = entry["item"]
            quantity = entry["quantity"]

            print(f"Food_ID : {item.Food_ID} , Food_Name : {item.Food_Name} , Price : {item.Price} , Quantity : {quantity} , Subtotal : {item.Price * quantity}")
        print(f"Total Price : {self.Total_Price}")

    def Calculate_Total(self):
        total = 0.0
        for entry in self.List_Of_SelectedItems:
            item = entry["item"]
            quantity = entry["quantity"]
            total = total + (item.Price * quantity)
        self.Total_Price = total
        return self.Total_Price

    def Empty_Cart(self):
        self.List_Of_SelectedItems = []
        self.Total_Price = 0.0
        print(" Cart Emptied.")
