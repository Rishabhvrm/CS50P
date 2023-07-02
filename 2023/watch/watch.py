import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # starts with <
    
    if matches := re.search(r"<.*https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
        return("https://youtu.be/" + matches.group(1))

if __name__ == "__main__":
    main()


# src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Y