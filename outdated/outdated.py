import re

# define months dictionary
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

# define variables
valid_date, spelled_date, numerical_date = False, False, False

# prompt user until valid date provided
while True:
    date = input("Date: ").strip()

    # check date format: month_digit/date_digit/year_digit
    # check if first element is a digit
    if re.search("/\d\/\d\/\d\d\d\d", date):
    #if date[0].isdigit():
        month, date, year = date.split('/')
        month, date = int(month), int(date)

        # validate month & date
        if 1<= month <= 12 and 1 <= date <= 31:
            valid_date = True
            numerical_date = True

    # check date format: month_spelled date_digit, year_digit
    # check if first element is a char
    elif date[0].isalpha():
        month, date, year = date.split(' ')
        # exclude comma(,) at end of date
        date = int(date[:-1])

        # validate month and date
        if month.title() in months.keys() and 1 <= date <= 31:
            valid_date = True
            spelled_date = True

    # if correct date format
    # break out of the loop
    if valid_date:
        break


# format the date
#if numerical_date:
#    print(f"{year}-{month:02}-{date:02}")

#if spelled_date:
#    print(f"{year}-{months[month]:02}-{date:02}")

print(f"{year}-{month:02}-{date:02}" if numerical_date else f"{year}-{months[month]:02}-{date:02}")