import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE)
    print(matches)
    if matches:
        print('yaya')
        return(matches.group(1))


if __name__ == "__main__":
    main()


# src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Y