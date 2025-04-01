# 🧾 Restaurant Ordering System

A simple terminal-based Python program that simulates a restaurant ordering experience. Customers can browse a menu, select items, specify quantities, and receive an itemized receipt with a final total.

---

## 🚀 Features

- 🧑‍🍳 Interactive ordering flow with menu numbers
- 🧾 Automatically formatted itemized receipts
- 🛒 Order multiple items with customizable quantities
- 💵 Dynamic price calculation
- 📋 Easily extendable menu structure

---

## 🗂️ Project Structure

| Function | Description |
|---------|-------------|
| `place_order(menu)` | Displays the menu, collects customer orders, and returns the final receipt and total |
| `update_order(order, menu_selection, menu_items)` | Validates user input and appends items to the order |
| `print_itemized_receipt(receipt)` | Prints each ordered item with price and quantity |
| `print_receipt_line()` | Helper to format each line of the receipt |
| `print_receipt_heading()` / `print_receipt_footer()` | Formats receipt headers/footers |
| `print_menu_heading()` / `print_menu_line()` | Formats menu display |
| `get_menu_items_dict(menu)` | Maps menu numbers to item names and prices |
| `get_menu_dictionary()` | Returns the nested dictionary of menu items |

---

## 🧪 Example Menu

```python
{
  "Burrito": {
    "Chicken": 4.49,
    "Beef": 5.49,
    "Vegetarian": 3.99
  },
  "Pizza": {
    "Cheese": 8.99,
    "Pepperoni": 10.99
  }
}
```

---

## 📦 How to Run

1. Clone the repository or download the script.
2. Open a terminal in the project directory.
3. Run the file using Python:

```bash
python3 order_system.py
```

Follow the prompts in the terminal to place your order.

---

## ✅ Sample Output

```text
Welcome to the Generic Take Out Restaurant.
What would you like to order?

Item # | Item name                        | Price
--------------------------------------------------
1      | Burrito - Chicken                | $4.49
2      | Burrito - Beef                   | $5.49
...

Type menu number: 1
What quantity of Burrito - Chicken would you like?
(This will default to 1 if number is not entered)

Would you like to keep ordering? (N) to quit: n

Thank you for your order.

Item name                       | Price  | Quantity
----------------------------------------------------
Burrito - Chicken              | $4.49  | 2
----------------------------------------------------
Total price: $8.98
----------------------------------------------------
```

---

## 📌 Notes

- All prices are hardcoded for simplicity but can easily be replaced with dynamic input.
- The menu structure supports as many categories and items as needed.
- Can be extended to support saving orders, delivery info, or tip calculations.

---

## 🧠 Author

Built as a beginner-friendly CLI application using Python. Great for learning input handling, dictionaries, loops, and formatting.