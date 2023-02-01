from collections import Counter, OrderedDict

# initialise an empty list
item_list = []

# keep prompting the user until CTRL + D
while True:

    try:
        item = input().strip()
    except EOFError:
        break
    else:
        # append to the list until CTRL + D
        item_list.append(item)

# use 'Counter' to count the occurance of each itme in the list
# convert it into a dict, store both value and occurance (we need both the values, hence dict)
# sort the dict using keys on dict.items, sorted returns a list
# convert it into a dict again
d = dict(sorted(dict(Counter(item_list)).items()))

# print value and key
for k,v in d.items():
    print(f"{v} {k.upper()}")