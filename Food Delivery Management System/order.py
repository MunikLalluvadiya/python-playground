import csv
from datetime import date


class Order:

    def __init__(self, Order_ID, User, Restaurant, Ordered_Items, Total_Amount):
        self.Order_ID = Order_ID
        self.User = User
        self.Restaurant = Restaurant
        self.Ordered_Items = Ordered_Items          
        self.Total_Amount = Total_Amount
        self.Order_Status = "Preparing"
        self.Order_Date = str(date.today())

    def Place_Order(self):
    
        items_str = ""
        for entry in self.Ordered_Items:
            item = entry["item"]
            quantity = entry["quantity"]
            if items_str != "":
                items_str = items_str + ";"
            items_str = items_str + f"{item.Food_ID}:{item.Food_Name}:{item.Price}:{quantity}"

        row = [self.Order_ID, self.User.Email, self.Restaurant.Restaurant_ID, items_str,
               self.Total_Amount, self.Order_Status, self.Order_Date]

        write_header = True
        with open("orders.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        with open("orders.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Order_ID", "User_Email", "Restaurant_ID", "Ordered_Items",
                                  "Total_Amount", "Order_Status", "Order_Date"])
            writer.writerow(row)

        print(f" Order {self.Order_ID} placed successfully. Status: {self.Order_Status}")

    def Cancel_Order(self):
        self.Order_Status = "Cancelled"

        rows = []
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == self.Order_ID:
                    row[5] = "Cancelled"
                if row:
                    rows.append(row)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Order {self.Order_ID} has been cancelled.")

    def View_Order(self):
        found = False
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row and row[0] == self.Order_ID:
                    found = True
                    print(f"Order_ID : {row[0]}")
                    print(f"User_Email : {row[1]}")
                    print(f"Restaurant_ID : {row[2]}")
                    print(f"Ordered_Items : {row[3]}")
                    print(f"Total_Amount : {row[4]}")
                    print(f"Order_Status : {row[5]}")
                    print(f"Order_Date : {row[6]}")
                    break

        if not found:
            print(" Order Not Found.")

    def Order_History(self):
        found = False
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row and row[1] == self.User.Email:
                    found = True
                    print(f"Order_ID : {row[0]} , Restaurant_ID : {row[2]} , "
                          f"Total_Amount : {row[4]} , Status : {row[5]} , Date : {row[6]}")

        if not found:
            print(" No previous orders found.")

    def Update_Status(self):
        print(" Status options: Preparing / Accepted / Out for Delivery / Delivered / Cancelled")
        new_status = input(" Enter New Status : ")
        self.Order_Status = new_status

        rows = []
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == self.Order_ID:
                    row[5] = new_status
                if row:
                    rows.append(row)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Order {self.Order_ID} status updated to {new_status}.")
