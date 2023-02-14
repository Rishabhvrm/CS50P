months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#while True:

date = input("Date: ")
is_date = False

# determine if date is in
# this format September 8, 1636
# or this 9/8/1636
if date[0].isdigit():
    if 1<= date[0] <= 12:
        is_date = True
        num_date = True


elif date[0].isalpha():
    a, b = date.split(' ', maxsplit=1)
    if a.title() in months:
        is_date = True
        word_date = True

# if date is in correct format
# break out of the loop
if is_date:
    # break
    pass


print(date[0])
print(a)
print(b)


# format the date
# if date is in format 9/8/1636
if num_date:
    month, date, year = date.split('/').strip()
    print(f"{year}-{month:02}-{date:02}")

if word_date:


# print out put
