import re
import sys

def main():
    # print(validate(input("IPv4 Address: ")))
    n = '300'
    if re.search(r"^([01]?[0-9]?[0-9]|2[0-4][0-9])$", n):
        print(True)
    else:
        print(False)


def validate(ip):
    return re.search(r"[0-255]\.[0-255]\.[0-255]\.[0-255]", ip)

if __name__ == "__main__":
    main()