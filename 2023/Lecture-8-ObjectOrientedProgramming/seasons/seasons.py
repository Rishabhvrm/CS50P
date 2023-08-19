from datetime import date
import sys

# expects date in YYYY-MM-DD format

def main():
    d = input("Date of Birth: ")

    try:
        date_obj = date.fromisoformat(d)
    except:
        sys.exit("Invalid date")
    else:
        a = (date_obj)
        b = (date.today())
        print(b - a)
        date_diff = calculate_minutes(date_obj)



def calculate_minutes(d):
    ...



if __name__ == "__main__":
    main()



"""

https://cs50.harvard.edu/python/2022/psets/8/seasons/



"""