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

while True:
    order = input("Item: ")
    current_order = order.title()
    print(current_order)
    if order in menu:
        break

total = 0

total += menu[current_order]
print(f"Total: ${total}")

EOFError