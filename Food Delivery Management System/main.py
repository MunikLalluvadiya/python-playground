from User import User
from restaurant import Restaurant, view_restaurants, search_restaurant, get_restaurant_basic_info
from Cart import Cart
from order import Order
from payment import CashOnDelivery, UPIPayment, CardPayment, Payment
from delivery import DeliveryAgent
from utils import calculate_bill


def profile_menu(user):
    PROFILE_MENU = """
------------------ MY PROFILE ------------------
 1. View Profile
 2. Update Profile
 3. Change Password
 4. Back
--------------------------------------------------
"""
    while True:
        print(PROFILE_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            user.View_Profile()

        elif choice == "2":
            user.Update_Profile()

        elif choice == "3":
            user.Change_Password()

        elif choice == "4":
            break

        else:
            print(" Invalid choice. Please try again.")



def add_restaurant_flow():
    # OBJECT OF RESTO.
    restaurant_id = input(" Enter Restaurant ID : ")
    restaurant_name = input(" Enter Restaurant Name : ")
    location = input(" Enter Location : ")
    rating = input(" Enter Rating : ")

    new_restaurant = Restaurant(restaurant_id, restaurant_name, location, rating)
    print(f" Restaurant '{restaurant_name}' created.")

    while True:
        add_more = input(" Add a food item to this restaurant? (yes/no) : ").strip().lower()
        if add_more == "yes":
            new_restaurant.Add_Food_Item()
        else:
            break


def manage_restaurant_flow():
    # Resto. menu
    restaurant_id = input(" Enter Restaurant ID to manage : ")
    name, location, rating = get_restaurant_basic_info(restaurant_id)

    if name is None:
        print(" That Restaurant ID was not found.")
        return

    restaurant_obj = Restaurant(restaurant_id, name, location, rating)

    MANAGE_MENU = """
--------------- MANAGE RESTAURANT ---------------
 1. Display Restaurant
 2. View Menu
 3. Add Food Item
 4. Remove Food Item
 5. Update Food Item
 6. Back
----------------------------------------------------
"""
    while True:
        print(MANAGE_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            restaurant_obj.Display_Restaurant()

        elif choice == "2":
            restaurant_obj.View_Menu()

        elif choice == "3":
            restaurant_obj.Add_Food_Item()

        elif choice == "4":
            restaurant_obj.Remove_Food_Item()

        elif choice == "5":
            restaurant_obj.Update_Food_Item()

        elif choice == "6":
            break

        else:
            print(" Invalid choice. Please try again.")


def restaurant_menu():
    RESTAURANT_MENU = """
------------------ RESTAURANTS ------------------
 1. View All Restaurants
 2. Search Restaurant
 3. Add New Restaurant
 4. Manage a Restaurant
 5. Back
--------------------------------------------------
"""
    while True:
        print(RESTAURANT_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            view_restaurants()

        elif choice == "2":
            search_restaurant()

        elif choice == "3":
            add_restaurant_flow()

        elif choice == "4":
            manage_restaurant_flow()

        elif choice == "5":
            break

        else:
            print(" Invalid choice. Please try again.")




def cart_menu(cart):
    CART_MENU = """
--------------------- CART ---------------------
 1. View Menu
 2. Add Item
 3. Remove Item
 4. Update Quantity
 5. View Cart
 6. Calculate Total
 7. Empty Cart
 8. Back
--------------------------------------------------
"""
    while True:
        print(CART_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            restaurant_id = input(" Enter Restaurant ID to view its menu : ")
            name, location, rating = get_restaurant_basic_info(restaurant_id)
            if name is None:
                print(" That Restaurant ID was not found.")
            else:
                restaurant_obj = Restaurant(restaurant_id, name, location, rating)
                restaurant_obj.View_Menu()

        elif choice == "2":
            cart.Add_Item()

        elif choice == "3":
            cart.Remove_Item()

        elif choice == "4":
            cart.Update_Quantity()

        elif choice == "5":
            cart.View_Cart()

        elif choice == "6":
            total = cart.Calculate_Total()
            print(f" Total Price : {total}")

        elif choice == "7":
            cart.Empty_Cart()

        elif choice == "8":
            break

        else:
            print(" Invalid choice. Please try again.")



def place_order_flow(user, cart):

    if len(cart.List_Of_SelectedItems) == 0:
        print(" Your cart is empty. Add some items first.")
        return

    restaurant_id = input(" Enter the Restaurant ID this order is from : ")
    name, location, rating = get_restaurant_basic_info(restaurant_id)

    if name is None:
        print(" That Restaurant ID was not found.")
        return

    restaurant_obj = Restaurant(restaurant_id, name, location, rating)

    subtotal = cart.Calculate_Total()
    delivery_charge, gst_amount, grand_total = calculate_bill(subtotal)

    print("\n --------- BILL --------- ")
    print(f" Restaurant Name : {restaurant_obj.Restaurant_Name}")
    print(f" Customer Name   : {user.Name}")
    print(" Ordered Items:")

    for entry in cart.List_Of_SelectedItems:
        item = entry["item"]
        quantity = entry["quantity"]
        print(f"   {item.Food_Name} x {quantity} = {item.Price * quantity}")
    print(f" Subtotal        : {subtotal}")
    print(f" Delivery Charge : {delivery_charge}")
    print(f" GST             : {gst_amount}")
    print(f" Grand Total     : {grand_total}")
    print(" ------------------------- \n")

    order_id = input(" Enter an Order ID for this order : ")
    new_order = Order(order_id, user, restaurant_obj, cart.List_Of_SelectedItems, grand_total)
    new_order.Place_Order()

    print("\n Choose Payment Method:")
    print(" 1. Cash on Delivery")
    print(" 2. UPI")
    print(" 3. Credit Card")
    print(" 4. Debit Card")
    payment_choice = input(" Enter choice : ").strip()

    payment_id = input(" Enter a Payment ID : ")

    if payment_choice == "1":
        payment_obj = CashOnDelivery(payment_id, order_id, grand_total)
    elif payment_choice == "2":
        payment_obj = UPIPayment(payment_id, order_id, grand_total)
    elif payment_choice == "3":
        payment_obj = CardPayment(payment_id, order_id, grand_total, "Credit Card")
    elif payment_choice == "4":
        payment_obj = CardPayment(payment_id, order_id, grand_total, "Debit Card")
    else:
        print(" Invalid payment choice. Order saved, but payment was not recorded.")
        return

    payment_obj.Make_Payment()
    payment_obj.Generate_Receipt()

    cart.Empty_Cart()


def order_menu(user, cart):
    ORDER_MENU = """
--------------------- ORDERS ---------------------
 1. Place Order
 2. Cancel Order
 3. View Order
 4. Order History
 5. Update Order Status
 6. View Payment Details
 7. Back
--------------------------------------------------
"""
    while True:
        print(ORDER_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            place_order_flow(user, cart)

        elif choice == "2":
            order_id = input(" Enter Order ID to cancel : ")
            temp_order = Order(order_id, user, None, [], 0)
            temp_order.Cancel_Order()

        elif choice == "3":
            order_id = input(" Enter Order ID to view : ")
            temp_order = Order(order_id, user, None, [], 0)
            temp_order.View_Order()

        elif choice == "4":
            # Order_History only needs self.User to filter by email,
            # so the other Order fields are just placeholders here.
            history_order = Order("", user, None, [], 0)
            history_order.Order_History()

        elif choice == "5":
            order_id = input(" Enter Order ID to update : ")
            temp_order = Order(order_id, user, None, [], 0)
            temp_order.Update_Status()

        elif choice == "6":
            payment_id = input(" Enter Payment ID to view : ")
            temp_payment = Payment(payment_id, "", "", 0)
            temp_payment.View_Payment_Details()

        elif choice == "7":
            break

        else:
            print(" Invalid choice. Please try again.")


def customer_dashboard(user):
   
    cart = Cart()

    DASHBOARD_MENU = """
--------------- CUSTOMER DASHBOARD ---------------
 1. My Profile
 2. Restaurants
 3. Cart
 4. Orders
 5. Logout
----------------------------------------------------
"""

    while True:
        print(DASHBOARD_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            profile_menu(user)

        elif choice == "2":
            restaurant_menu()

        elif choice == "3":
            cart_menu(cart)

        elif choice == "4":
            order_menu(user, cart)

        elif choice == "5":
            print(" Logged out.")
            break

        else:
            print(" Invalid choice. Please try again.")


def delivery_agent_menu():
    """Lets a delivery agent log in and manage deliveries."""
    agent_id = input(" Enter Agent ID : ")
    name = input(" Enter Your Name : ")
    phone_number = input(" Enter Phone Number : ")
    vehicle_number = input(" Enter Vehicle Number : ")

    agent = DeliveryAgent(agent_id, name, phone_number, vehicle_number)

    AGENT_MENU = """
--------------- DELIVERY AGENT MENU ---------------
 1. Accept Delivery
 2. Update Delivery Status
 3. Complete Delivery
 4. Logout
----------------------------------------------------
"""

    while True:
        print(AGENT_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            agent.Accept_Delivery()

        elif choice == "2":
            agent.Update_Delivery_Status()

        elif choice == "3":
            agent.Complete_Delivery()

        elif choice == "4":
            print(" Logged out.")
            break

        else:
            print(" Invalid choice. Please try again.")



def main():
    MAIN_MENU = """
==================== FOOD DELIVERY SYSTEM ====================
 1. Register
 2. Login
 3. Delivery Agent Login
 4. Exit
================================================================
"""

    while True:
        print(MAIN_MENU)
        choice = input(" Enter your choice : ").strip()

        if choice == "1":
            user = User()
            user.Register()
            customer_dashboard(user)

        elif choice == "2":
            user = User()
            login_success = user.Login()
            if login_success:
                customer_dashboard(user)

        elif choice == "3":
            delivery_agent_menu()

        elif choice == "4":
            print(" Exiting. Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")


main()