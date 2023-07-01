import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #
    regex = "([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    # return True if re.search(rf"^{regex}\.{regex}\.{regex}\.{regex}$", ip) else False
    matches = re.search(rf"^{regex}\.{regex}\.{regex}\.{regex}$", ip)
    print(matches.group(1), matches.group(2))

if __name__ == "__main__":
    main()