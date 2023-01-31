item_list = []

while True:

    try:
        item = input().strip()
    except EOFError:
        break
    else:
        item_list.append(item)

print(item_list)