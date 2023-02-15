months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

is_date = False
word_date, num_date = False, False

while True:
    date = input("Date: ").strip()

    # determine if date is in
    # this format: 9/8/1636
    # check if first char is a number
    if date[0].isdigit():
        # check valid month
        if 1<= int(date[0]) <= 12:
            num_date = True
            month, date, year = date.split('/')
            if 1 <= int(date) <= 31:
                is_date = True


    # determine if date is in
    # this format: September 8, 1636
    elif date[0].isalpha():
        a, b = date.split(' ', maxsplit=1)
        if a.title() in months.keys():
            is_date = True
            word_date = True

    # if date is in correct format
    # break out of the loop
    if is_date:
        break
        #pass

#print(a)
#print(b)


# format the date
# if date is in format 9/8/1636
if num_date:

    print(f"{year}-{month.zfill(2)}-{date.zfill(2)}")

if word_date:
    month, date, year = date.split(' ')
    print(f"{year}-{months[month]:02}-{date[:-1].zfill(2)}")


# print output
