import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # 0 or 1, 1 to 9, 1 to 9 (0-199) OR 2, 0 to 4, 0 to 9 ()
    regex = "([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    return True if re.search(rf"^{regex}\.{regex}\.{regex}\.{regex}$", ip) else False

if __name__ == "__main__":
    main()