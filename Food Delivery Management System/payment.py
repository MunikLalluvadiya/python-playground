import csv


class Payment:

    def __init__(self, Payment_ID, Order_ID, Payment_Method, Amount):
        self.Payment_ID = Payment_ID
        self.Order_ID = Order_ID
        self.Payment_Method = Payment_Method
        self.Payment_Status = "Pending"
        self.Amount = Amount

    def Make_Payment(self):
        self.Payment_Status = "Paid"

        row = [self.Payment_ID, self.Order_ID, self.Payment_Method, self.Payment_Status, self.Amount]

        write_header = True
        with open("payments.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        with open("payments.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Payment_ID", "Order_ID", "Payment_Method", "Payment_Status", "Amount"])
            writer.writerow(row)

        print(f" Payment of {self.Amount} recorded as {self.Payment_Status} via {self.Payment_Method}.")

    def Generate_Receipt(self):
        print(" ----- RECEIPT ----- ")
        print(f" Payment_ID : {self.Payment_ID}")
        print(f" Order_ID : {self.Order_ID}")
        print(f" Payment_Method : {self.Payment_Method}")
        print(f" Payment_Status : {self.Payment_Status}")
        print(f" Amount : {self.Amount}")
        print(" -------------------- ")

    def View_Payment_Details(self):
        found = False
        with open("payments.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            for row in reader:
                if row and row[0] == self.Payment_ID:
                    found = True
                    print(f"Payment_ID : {row[0]} , Order_ID : {row[1]} , Payment_Method : {row[2]} , Payment_Status : {row[3]} , Amount : {row[4]}")

        if not found:
            print(" Payment Not Found.")


class CashOnDelivery(Payment):
    def __init__(self, Payment_ID, Order_ID, Amount):
        super().__init__(Payment_ID, Order_ID, "Cash on Delivery", Amount)

    def Make_Payment(self):
        
        print(" Cash on Delivery selected. Please keep exact change ready for the delivery agent.")
        self.Payment_Status = "Pending"

        row = [self.Payment_ID, self.Order_ID, self.Payment_Method, self.Payment_Status, self.Amount]

        write_header = True
        with open("payments.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        with open("payments.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Payment_ID", "Order_ID", "Payment_Method", "Payment_Status", "Amount"])
            writer.writerow(row)


class UPIPayment(Payment):
    def __init__(self, Payment_ID, Order_ID, Amount):
        super().__init__(Payment_ID, Order_ID, "UPI", Amount)

    def Make_Payment(self):
        upi_id = input(" Enter your UPI ID : ")
        print(f" Processing UPI payment of {self.Amount} using {upi_id}...")

        self.Payment_Status = "Paid"

        row = [self.Payment_ID, self.Order_ID, self.Payment_Method, self.Payment_Status, self.Amount]

        write_header = True
        with open("payments.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        with open("payments.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Payment_ID", "Order_ID", "Payment_Method", "Payment_Status", "Amount"])
            writer.writerow(row)

        print(f" Payment of {self.Amount} recorded as {self.Payment_Status} via {self.Payment_Method}.")


class CardPayment(Payment):
    def __init__(self, Payment_ID, Order_ID, Amount, card_type):
        super().__init__(Payment_ID, Order_ID, card_type, Amount)

    def Make_Payment(self):
        card_number = input(" Enter your Card Number : ")
        last_four = card_number[-4:]
        print(f" Processing {self.Payment_Method} payment of {self.Amount} using card ending in {last_four}...")

        self.Payment_Status = "Paid"

        row = [self.Payment_ID, self.Order_ID, self.Payment_Method, self.Payment_Status, self.Amount]

        write_header = True
        with open("payments.csv", "r", newline="") as file:
            if file.readline().strip() != "":
                write_header = False

        with open("payments.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["Payment_ID", "Order_ID", "Payment_Method", "Payment_Status", "Amount"])
            writer.writerow(row)

        print(f" Payment of {self.Amount} recorded as {self.Payment_Status} via {self.Payment_Method}.")
