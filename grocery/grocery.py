from collections import Counter

item_dict = dict()


while True:

    try:
        item = input().strip()
    except EOFError:
        break
    else:
        item_list.append(item)

print(Counter(item_list))