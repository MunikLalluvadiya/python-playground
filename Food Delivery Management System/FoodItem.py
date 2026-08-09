class FoodItem:

    def __init__(self, Food_ID, Food_Name, Category, Price, Availability):
        self.Food_ID = Food_ID
        self.Food_Name = Food_Name
        self.Category = Category
        self.Price = Price
        self.Availability = Availability

    def Display_Food_Details(self):
        print(f"Food_ID : {self.Food_ID} , Food_Name : {self.Food_Name} , Category : {self.Category} , Price : {self.Price} , Availability : {self.Availability}")

    def Update_Price(self, new_price):
        self.Price = new_price

    def Update_Availability(self, new_status):
        self.Availability = new_status
