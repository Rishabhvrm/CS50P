from datetime import date
import sys

# expects date in YYYY-MM-DD format

def main():
    date = input("Date of Birth: ")

    try:
        date_obj = date.fromisoformat(date)
    except:
        sys.exit("Invalid date")
    else:
        date_diff = calculate_minutes(date_obj)



def calculate_minutes(date):
    ...



if __name__ == "__main__":
    main()



"""

https://cs50.harvard.edu/python/2022/psets/8/seasons/



"""