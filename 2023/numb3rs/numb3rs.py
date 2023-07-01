import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"[1-255]\.[1-255]\.[1-255]\.", ip)


if __name__ == "__main__":
    main()