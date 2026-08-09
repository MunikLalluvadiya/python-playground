import csv
from FoodItem import FoodItem


def view_restaurants():
    found_any = False
    with open("restaurant.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row:
                found_any = True
                print(f"Restaurant_ID : {row[0]} , Restaurant_Name : {row[1]} , Location : {row[2]} , Rating : {row[3]}")

    if not found_any:
        print(" No restaurants available yet.")


def search_restaurant():
    
    search_text = input(" Enter restaurant name to search : ").strip().lower()
    found_any = False
    with open("restaurant.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row and search_text in row[1].lower():
                found_any = True
                print(f"Restaurant_ID : {row[0]} , Restaurant_Name : {row[1]} , Location : {row[2]} , Rating : {row[3]}")

    if not found_any:
        print(" No matching restaurant found.")


def get_restaurant_basic_info(restaurant_id):
    
    with open("restaurant.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row and row[0] == restaurant_id:
                return row[1], row[2], row[3]
    return None, None, None



class Restaurant:

    def __init__(self, Restaurant_ID, Restaurant_Name, Location, Rating):
        self.Restaurant_ID = Restaurant_ID
        self.Restaurant_Name = Restaurant_Name
        self.Location = Location
        self.Rating = Rating
        self.List_Of_FoodItems = []

        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for row in reader:
                if row and row[0] == self.Restaurant_ID:
                    items_str = row[4]
                    if items_str:
                        for item_str in items_str.split(";"):
                            food_id, food_name, category, price, availability = item_str.split(":")
                            self.List_Of_FoodItems.append(
                                FoodItem(food_id, food_name, category, float(price), availability == "True")
                            )
                    break

    def Display_Restaurant(self):
        found = False
        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row and row[0] == self.Restaurant_ID:
                    found = True
                    restaurant_id, name, location, rating, items_str = row
                    print(f"Restaurant_ID : {restaurant_id} , Restaurant_Name : {name} , "
                          f"Location : {location} , Rating : {rating}")
                    if items_str:
                        for item_str in items_str.split(";"):
                            food_id, food_name, category, price, availability = item_str.split(":")
                            print(f"    Food_ID : {food_id} , Food_Name : {food_name} , "
                                  f"Category : {category} , Price : {price} , "
                                  f"Availability : {availability}")
                    else:
                        print("    (No food items yet.)")
                    break

        if not found:
            print(" Deta NotFound! ")

    def Add_Food_Item(self):
        Food_ID = input(" Enter Food ID : ")
        Food_Name = input(" Enter Food Name : ")
        Category = input(" Enter Food Category : ")
        Price = float(input(" Enter Food Price : "))
        Availability = input(" Enter Availability (yes/no) : ").strip().lower() in ("yes", "y", "true")

        new_item = FoodItem(Food_ID, Food_Name, Category, Price, Availability)
        self.List_Of_FoodItems.append(new_item)


        rows = []
        found = False
        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == self.Restaurant_ID:
                    found = True
                else:
                    rows.append(row)

        items_str = ""
        for i in self.List_Of_FoodItems:
            if items_str != "":
                items_str = items_str + ";"
            items_str = items_str + f"{i.Food_ID}:{i.Food_Name}:{i.Category}:{i.Price}:{i.Availability}"

        if not rows:
            rows.append(["Restaurant_ID", "Restaurant_Name", "Location", "Rating", "Food_Items"])
        rows.append([self.Restaurant_ID, self.Restaurant_Name, self.Location, self.Rating, items_str])

        with open("restaurant.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"Added {Food_Name} to {self.Restaurant_Name}'s menu.")

    def Remove_Food_Item(self):
        food_id = input(" Enter Food ID to remove : ")

        found = False
        for item in self.List_Of_FoodItems:
            if item.Food_ID == food_id:
                self.List_Of_FoodItems.remove(item)
                found = True
                break

        if not found:
            print(" Deta NotFound! ")
            return

       
        rows = []
        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] != self.Restaurant_ID:
                    rows.append(row)

        items_str = ""
        for i in self.List_Of_FoodItems:
            if items_str != "":
                items_str = items_str + ";"
            items_str = items_str + f"{i.Food_ID}:{i.Food_Name}:{i.Category}:{i.Price}:{i.Availability}"

        if not rows:
            rows.append(["Restaurant_ID", "Restaurant_Name", "Location", "Rating", "Food_Items"])
        rows.append([self.Restaurant_ID, self.Restaurant_Name, self.Location, self.Rating, items_str])

        with open("restaurant.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Removed food item {food_id}.")

    def Update_Food_Item(self):
        food_id = input(" Enter Food ID to update : ")

        target_item = None
        for item in self.List_Of_FoodItems:
            if item.Food_ID == food_id:
                target_item = item
                break

        if target_item is None:
            print(" Deta NotFound! ")
            return

        choice = input(" Update (1) Price or (2) Availability? : ").strip()
        if choice == "1":
            new_price = float(input(" Enter new price : "))
            target_item.Update_Price(new_price)
        elif choice == "2":
            avail_input = input(" Available? (yes/no) : ").strip().lower()
            target_item.Update_Availability(avail_input in ("yes", "y", "true"))
        else:
            print(" Invalid choice.")
            return

        # write this restaurant's current state straight to restaurant.csv
        rows = []
        with open("restaurant.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] != self.Restaurant_ID:
                    rows.append(row)

        items_str = ""
        for i in self.List_Of_FoodItems:
            if items_str != "":
                items_str = items_str + ";"
            items_str = items_str + f"{i.Food_ID}:{i.Food_Name}:{i.Category}:{i.Price}:{i.Availability}"

        if not rows:
            rows.append(["Restaurant_ID", "Restaurant_Name", "Location", "Rating", "Food_Items"])
        rows.append([self.Restaurant_ID, self.Restaurant_Name, self.Location, self.Rating, items_str])

        with open("restaurant.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Updated food item {food_id}.")

    def View_Menu(self):
        if not self.List_Of_FoodItems:
            print(" (No food items yet.)")
            return
        for item in self.List_Of_FoodItems:
            item.Display_Food_Details()