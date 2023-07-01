import re
import sys

def main():
    # print(validate(input("IPv4 Address: ")))
    n = '123'
    if re.search(r"", n):
        print(True)
    else:
        print(False)


def validate(ip):
    return re.search(r"[0-255]\.[0-255]\.[0-255]\.[0-255]", ip)

if __name__ == "__main__":
    main()