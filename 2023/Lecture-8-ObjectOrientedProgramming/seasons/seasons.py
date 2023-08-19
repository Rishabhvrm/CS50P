from datetime import date
import sys
import inflect
p = inflect.engine()



def main():
    try:
        # expects date in YYYY-MM-DD format
        date_obj = date.fromisoformat(input("Date of Birth: "))
    except:
        sys.exit("Invalid date")
    else:
        print(calculate_minutes(date_obj), "minutes")


def calculate_minutes(d_obj):
    diff = date.today() - d_obj                         # calculate difference between today and given date
    minutes = (diff.days * 24 * 60)                     # convert days into minutes
    return p.number_to_words(minutes, andword="")       # use inflect to convert number to words

if __name__ == "__main__":
    main()



"""

https://cs50.harvard.edu/python/2022/psets/8/seasons/



"""