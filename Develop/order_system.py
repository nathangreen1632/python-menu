def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.
    """
    global order_total
    order = []
    menu_items = get_menu_items_dict(menu)

    print("Welcome to the Generic Take Out Restaurant.")
    print("What would you like to order? ")

    place_ordering = True

    while place_ordering:
        print_menu_heading()

        menu_number = 1
        for category, options in menu.items():
            for meal, price in options.items():
                print_menu_line(menu_number, category, meal, price)
                menu_number += 1

        menu_selection = input("Type menu number: ")

        order = update_order(order, menu_selection, menu_items)

        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")

        if keep_ordering.lower() == 'n':
            print("Thank you for your order.")

            prices_list = [item["Price"] * item["Quantity"] for item in order]
            order_total = round(sum(prices_list), 2)

            place_ordering = False  # Exit loop

    return order, order_total



def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.
    """
    if not menu_selection.isdigit():
        print(f"{menu_selection} was not a menu option.")
        return order



    menu_selection = int(menu_selection)

    if menu_selection not in menu_items:
        print("Sorry, that item is not on the menu.")
        return order

    item_name = menu_items[menu_selection]['Item name']
    item_price = menu_items[menu_selection]["Price"]

    print(f"What quantity of {item_name} would you like? ")
    print("(This will default to 1 if number is not entered)")
    quantity_input = input()

    try:
        quantity = int(quantity_input)
        if quantity < 1:
            print("Invalid quantity. Adding 1 by default.")
            quantity = 1
    except ValueError:
        print("Invalid quantity. Adding 1 by default.")
        quantity = 1

    order.append({
        'Item name': item_name,
        "Price": item_price,
        "Quantity": quantity
    })

    return order



def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.
    """
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        print_receipt_line(item_name, price, quantity)


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    menu_items = {}

    i = 1

    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items


def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """

    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

if __name__ == "__main__":
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    print("This is what we are preparing for you.\n")

    print_receipt_heading()

    print_itemized_receipt(receipt)

    print_receipt_footer(total_price)

