import re

def main():
    print(convert(input("Hours: ")))

# allowed input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
def convert(time):
    if (re.search(r"^\d{1,2}:\d{1,2} AM to \d{1,2}:\d{1,2} PM$", time)):
        print('Yayy')
    else: print('Nayy')




if __name__ == "__main__":
    main()