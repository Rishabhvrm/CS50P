# making this file demonstrate
# > use of dictionaries

# checking what does a for loop prints for dictionaries
# > ANS - it prints KEYS
# note - comma at the last line is valid
dic = {
    "Name": "Tyler",
    "Occupation": "Soap Maker",
    "Friend": "Narrator",
}

# OUTPUT will print only the keys no matter what the name of the variable is in the loop
for value in dic:
    print(value)

# outputs keys and values both
for key in dic:
    print(key, dic[key])

# outputs keys and values both
for k,v in dic.items():
    print(k + ": " + v)


# SORTING THE DICTIONARY

# this gives the list of tuples sorted by keys
sorted_keys_list = sorted(dic.items())
print(sorted_keys_list)

# converts the list of tuples into a dictionary
sorted_dict = dict(sorted_keys_list)
print(sorted_dict)