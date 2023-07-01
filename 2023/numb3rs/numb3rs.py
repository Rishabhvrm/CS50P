import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
    # n = '256'
    # if re.search(r"^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$", n):
    #     print(True)
    # else:
    #     print(False)


def validate(ip):
    regex = "^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"
    return re.search(rf"{regex}\.{regex}\.{regex}\.{regex}", ip)

if __name__ == "__main__":
    main()