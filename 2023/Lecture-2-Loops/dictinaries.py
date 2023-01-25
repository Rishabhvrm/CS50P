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