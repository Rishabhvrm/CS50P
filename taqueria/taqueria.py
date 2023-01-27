# initialize menu and total
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

# prompt the user until EOF (Ctrl + D) happens
while True:
    try:
        order = input("Item: ")
    except EOFError:
        break
    else:
        # convert the order to title case
        current_order = order.title()

        # check if item is in menu
        # add to total
        if current_order in menu:
            total += menu[current_order]
            print(f"Total: ${total:.2f}")




