import re

def main():
    print(convert(input("Hours: ")))

# allowed input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
def convert(time):
    if (re.search(r"^\d{12}:\d{12} AM to \d{12}:\d{12} PM", time)):
        print('Yayy')
    else: print('Nayy')




if __name__ == "__main__":
    main()