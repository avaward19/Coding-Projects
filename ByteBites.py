# Ava Ward, sec 0104

import time

# Title
app_name = "ByteBites"
# Menu
'''
The menu is a dictionary of products that contains nested dictionaries 
for each product's name and price.
'''
menu = {1: {'name':'Hamburger','price':6.55}, 
        2: {'name':'Cheeseburger','price':7.75},
        3: {'name':'Milkshake','price':5.75}, 
        4: {'name':'Fries','price':2.15},
        5: {'name':'Sub','price':6.15},
        6: {'name':'Ice Cream','price':1.55},
        7: {'name':'Fountain Drink','price':3.45}, 
        8: {'name':'Cookie','price':3.15},
        9: {'name':'Brownie','price':2.55}, 
        10: {'name':'Sauce','price':0.75}
       }
# Actions 
'''
A dictionary of various actions a user can take while using the app
''' 
actions = {1:'Add a new menu item to cart', 
           2:'Remove an item from cart',
           3:'Modify a cart item\'s quantity', 
           4:'View cart',
           5:'Checkout', 
           6:'Logout'
          }
# sales tax
sales_tax = 0.05
# Cart
'''
The cart is being initialized as an empty dictionary, and can be modified
by the user while they use the app
'''
cart = {}

# Simple user database
users = {
    'user1': {'password': 'password1', 'status': 'gold', 'student': True},
    'user2': {'password': 'password2', 'status': 'silver', 'student': False},
    'user3': {'password': 'password3', 'status': 'bronze', 'student': True}
}

# Login
def user_login():
    """
    Prompts the user for a username and password and authenticates them.
    
    Returns 
    -------
    True if authentication is successful, False otherwise.

    username: str
    """
    print("\n    **** User Login ****\n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username]['password'] == password:
        print("\nLogin successful!")
        return True, username
    else:
        print("\nInvalid username or password.")
        return False, username

# New user
def create_new_user():
    """
    Allows a new user to register with a username and password.
    Updates the user database with the new credentials.

    Returns
    -------
    username: str
    """
    print("\n     **** Create New User ****\n")
    while True:
        username = input("Choose a username: ")
        if username in users:
            print("\nUsername already exists. Please choose a different username.")
        else:
            break

    password = input("Choose a password: ")
    users[username] = {'password': password}
    users[username]['status'] = 'member'
    while True:
        student = input("Are you a student? (y or n) ")
        if student.lower() == 'y':
            users[username]['student'] = True
            break
        elif student.lower() == 'n':
            users[username]['student'] = False
            break
        else:
            print("\nInvalid input.")
    print("\nUser registered successfully!\n")
    login, username = user_login()
    return login, username

# Discounts 
def apply_discount(status, is_student, current_total):
    """
    Discounts are applied based on membership status and if user is a student.

    Parameters
    ----------
    status: str
        user's membership status (gold, silver, bronze, member)
    
    is_student: bool
        True if user is student, False if user is not a student

    current_total: float
        cost of order before discounts are applied

    Returns
    -------
    total: float
        new cost with discounts applied
    """
    discount = 0
    if status == 'gold':
        discount += 2
        print("\nOur gold members get $2 off today!") # gold rewards
    elif status == 'silver':
        discount += 1
        print("\nOur silver members get $1 off today!") # silver rewards
    elif status == 'bronze':
        discount += 0.5
        print("\nOur bronze members get $0.50 off today!") # bronze rewards
    else:
        print("\nYou do not have any membership rewards today.") # no rewards
    if not current_total < discount: # if the discount is greater than the total cost, discount will not be applied
        total = current_total - discount
    else:
        total = current_total
    if is_student:
        total = total - (total*0.1) # student discount
        print("Your 10% Student discount has been applied.")
    return total

# Display menu and prices
def display_menu():
    """
    Displays the menu items and their respective prices
    to the user, associated with an integer.
    """
    print("\n     **** MENU ****\n")
    for item in menu:
        item_name = menu[item]['name'] # name of item
        item_price = menu[item]['price'] # price of item
        print(f'({item}) {item_name}: ${item_price}') # print full menu item

# Display available actions
def display_actions():
    """
    Displays all the actions the user is able to take
    while ordering, associated with an integer.
    """
    print("\n\n\n\n\n     **** Ordering Actions ****\n")
    for action in actions:
        action_statement = actions[action] # action is the number the user will input;
        print(f'({action}) {action_statement}') # action_statement is what the user is choosing to do

# Add item to cart  
def add_to_cart(item, quantity=1):
    """
    Adds the entered item and quantity to the cart.
    
    Parameters
    ----------
    item: str
        The number associated with menu item
    
    quantity: int
        The quantity of that item being added to cart (default 1)
    """
    if item not in menu: # user entered a value not on the menu
        print("\nI'm sorry, that is not an item on our menu.")
    else:
        if item in cart: # checks to see if item is already in cart then adds to that quantity
            cart[item] =+ quantity
        else:
            cart[item] = quantity
        print("\nAdded", quantity, "x", menu[item]['name'], "to the cart.") # Tells the user how much of chosen item was added to cart

# Remove item from cart
def remove_from_cart(item):
    """
    Removes the entered item from the cart if it exists.
    
    Parameters
    ----------
    item: int
        The number associated with menu item
    """
    if item not in cart: # user entered a value not in cart
        print("\nThis item is not currently in the cart.")
    else:
        cart.pop(item) # removes key and value from cart
        print("\nRemoved", menu[item]['name'], "from the cart.") # Tells the user what item was removed from cart

# Modify quantities of items in cart
def modify_cart(item, quantity):
    """
    Modifies the cart by updating the entered item
    with the entered quantity.
    
    Parameters
    ----------
    item: int
        The number associated with menu item
    
    quantity: int
        The new quantity of the item
    """
    if item not in cart: # user entered a value not in cart
        print("\nThis item is not currently in your cart.")
    else:
        if quantity > 0: # positive integer
            cart[item] = quantity # update quantity to value entered by user
            print("\nModified", menu[item]['name'], "quantity to", quantity, "in the cart.") # tell user what was modified
        else: # zero or negative means user wants to remove the item from cart
            remove_from_cart(item)

# View cart
def view_cart(username):
    """
    Displays the current cart items and quantities
    and the current subtotal of items in the cart.

    Parameters
    ----------
    username: str
        username used to get membership status of user
    """
    print("\n\n\n     **** Cart Contents ****\n") 
    subtotal = 0
    for item in cart: # loops through each item in the cart
        if item in menu:
            quantity = cart[item]
            subtotal += menu[item]['price'] * quantity # calculates each item price times its quantity
            print(quantity, "x", menu[item]['name'])
    tax = subtotal * sales_tax 
    subtotal = apply_discount(users[username]['status'], users[username]['student'], subtotal) # apply discounts
    total = round((subtotal + tax),2) # Calculates the total cost, factoring in the sales tax
    print("Total: $", total)

# Checkout
def checkout(username):
    """
    Displays the user's cart and indicates the order
    has been received.
    
    Parameters
    ----------
    username: str
        username used to get membership status of user
    """
    print("\n\n\n\n\n     **** Checkout ****")
    view_cart(username)
    process_payment()
    order_status_updates()

# Payment
def process_payment():
    """
    Processes the payment by credit/debit card. Prompts user to enter card details.
    Validates the length of the card number, expiration date, and security code.
    """
    print("\n     **** Payment ****\n")

    while True:
        # collect card information
        card_number = input("Enter your 16-digit card number: ") # arbitrary
        if len(card_number) != 16 or not card_number.isdigit():
            print("Invalid card number. Please enter a 16-digit card number.")
            continue

        expiration_date = input("Enter your card's 4-digit expiration date (MMYY): ") # must be valid, nonexpired date
        if len(expiration_date) != 4 or not expiration_date.isdigit():
            print("Invalid expiration date. Please enter a 4-digit expiration date.")
            continue
        elif int(expiration_date[0:2]) > 12 or int(expiration_date[0:2]) < 1 or int(expiration_date[2:len(expiration_date)]) < 24:
            print("Expired card or invalid expiration date. Please enter a valid expiration date.")
            continue

        security_code = input("Enter your card's 3-digit security code: ") # arbitrary
        if len(security_code) != 3 or not security_code.isdigit():
            print("Invalid security code. Please enter a 3-digit security code.")
            continue

        # If all inputs are valid
        print("\nProcessing your payment...\n")
        time.sleep(4)
        print("\n Payment successful! Thank you for your order.")
        break

# Alerts user when order ready for pick-up
def order_status_updates():
    """
    Provides real-time updates on the order status.
    """
    statuses = ["Order Received", "Preparing", "Ready for Pickup"]
    
    for status in statuses:
        print(f"\n\n\n\n\n Order Status: {status}")
        time.sleep(4)  # Simulates a wait time between status updates

    print("\nYour order is ready for pickup!\n")

# Ask for user input
def get_item_and_quantity(item_prompt, quantity_prompt=None):
    """
    Prompts the user for input 
    
    Parameters
    ----------
    item_prompt: str
        The prompt to display to the user before they enter the item number.
    
    quantity_prompt: str
        The prompt to display to the user before they enter the quantity.
        This defaults to None for cases where quanitity input is not needed.
        
    Returns
    -------
    item: int
    quantity: int
        The item value and the quantity (in certain cases)
    """
    item_input = input(item_prompt) # get item from user with prompt passed as argument into function
    item = int(item_input) # convert input to integer
    if quantity_prompt: # check for a quantity prompt; if none, user will not be asked to provide a quantity
        quantity_input = input(quantity_prompt)
        if quantity_input.isdigit(): # check if quantity input is a valid digit; if not, default to 1
            quantity = int(quantity_input)
        else:
            quantity = 1
        return item, quantity
    else:
        return item
    
# Ordering
def order_loop():
    """
    The main loop that runs while the user is ordering.
    """
    print("\n     Welcome to", app_name,"\n")

    # User login
    while True:
        print("1. Login\n2. Create New User\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            login, username = user_login()
            if login:
                break  # Exit loop if login is successful
        elif choice == '2':
            login, username = create_new_user()
            if login:
                break
        elif choice == '3':
            return  # Exit the application
        else:
            print("Invalid choice. Please try again.")

    ordering = True
    while ordering:
        display_actions()
        user_action = input("\nWhat would you like to do? ")
        if user_action == '1':
            display_menu()
            item, quantity = get_item_and_quantity("\nPlease enter the item number for the menu item you want to order: ","\nHow many would you like? ")
            add_to_cart(item, quantity)
        elif user_action == '2':
            display_menu()
            item = get_item_and_quantity("\nWhich item would you like to remove from your cart? ")
            remove_from_cart(item)
        elif user_action == '3':
            display_menu()
            item, quantity = get_item_and_quantity("\nWhich item in your cart do you wish to modify? ", "\nWhat would you like the new quantity for this item to be? ")
            modify_cart(item, quantity)
        elif user_action == '4':
            view_cart(username)
        elif user_action == '5':
            if cart == {}:
                print("\nYour cart is empty. Please add an item to proceed to checkout.")
            else:
                checkout(username)
                cart.clear()
                ordering = False
        elif user_action == '6':
            cart.clear()
            ordering == False
            break
        else:
            print("\nThat is not an available action.")
            continue

order_loop()


        
