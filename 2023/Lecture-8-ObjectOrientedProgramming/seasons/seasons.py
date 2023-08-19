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
        date_diff =
        print(calculate_minutes(date_obj), "minutes")


def calculate_minutes(d_obj):
    a = (d_obj)
    b = (date.today())
    c = (b - a)
    minutes = (c.days * 24 * 60)
    words = p.number_to_words(minutes, andword="")
    return (words)



if __name__ == "__main__":
    main()



"""

https://cs50.harvard.edu/python/2022/psets/8/seasons/



"""