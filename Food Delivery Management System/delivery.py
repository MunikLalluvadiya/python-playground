import csv


class DeliveryAgent:

    def __init__(self, Agent_ID, Name, Phone_Number, Vehicle_Number, Availability=True):
        self.Agent_ID = Agent_ID
        self.Name = Name
        self.Phone_Number = Phone_Number
        self.Vehicle_Number = Vehicle_Number
        self.Availability = Availability

    def Accept_Delivery(self):
        order_id = input(" Enter Order ID to accept : ")
        self.Availability = False

        rows = []
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == order_id:
                    row[5] = "Accepted"
                if row:
                    rows.append(row)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Agent {self.Name} accepted Order {order_id}. Status set to Accepted.")

    def Update_Delivery_Status(self):
        order_id = input(" Enter Order ID : ")
        new_status = input(" Enter New Status (e.g. Out for Delivery) : ")

        rows = []
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == order_id:
                    row[5] = new_status
                if row:
                    rows.append(row)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f" Order {order_id} status updated to {new_status}.")

    def Complete_Delivery(self):
        order_id = input(" Enter Order ID to complete : ")

        rows = []
        with open("orders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                rows.append(header)
            for row in reader:
                if row and row[0] == order_id:
                    row[5] = "Delivered"
                if row:
                    rows.append(row)

        with open("orders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        self.Availability = True
        print(f" Order {order_id} marked as Delivered. Agent {self.Name} is now available.")
