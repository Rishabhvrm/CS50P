from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    try:
        # expects date in YYYY-MM-DD format
        d = input("Date of Birth: ")
    except:
        raise ValueError
        sys.exit("Invalid date")
    else:
        # print(calculate_minutes(date_obj).capitalize(), "minutes")
        print(calculate_minutes(d))

def calculate_minutes(d):
    d_obj = date.fromisoformat(d)
    diff = date.today() - d_obj                         # calculate difference between today and given date
    minutes = (diff.days * 24 * 60)                     # convert days into minutes

    # use inflect to convert number to words
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()



"""

https://cs50.harvard.edu/python/2022/psets/8/seasons/



"""