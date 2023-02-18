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

    # check date format: month_digit/date_digit/year_digit, use regex to match d/d/dddd
    # check if first element is a digit
    if re.search("\d\/\d\/\d\d\d\d", date):
        month, date, year = date.split('/')
        month, date = int(month), int(date)                            # convert to int

        if 1<= month <= 12 and 1 <= date <= 31:                        # validate month & date
            valid_date = True
            numerical_date = True

    # check date format: month_spelled date_digit, year_digit (use regex)
    # check if first element is a char
    elif date[0].isalpha():
        if re.search("[a-zA-z]\s\d\,\s\d\d\d\d", date):
            month, date, year = date.split(' ')
            month = month.title()                                      # use title() to match the dictionary keys
            date = int(date[:-1])                                      # exclude comma(,) at end of date

            if month in months.keys() and 1 <= date <= 31:             # validate month and date
                valid_date = True
                spelled_date = True

    if valid_date:                                                     # if correct date format, break out of loop
        break

# print date conditionally, if it is numerical or spelled
print(f"{year}-{month:02}-{date:02}" if numerical_date else f"{year}-{months[month]:02}-{date:02}")