import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # starts with <
    # may have 0 or more characters after that
    # must have http, s is optional (? is 0 or 1)
    # must have ://
    # www. is optional (? is 0 or 1)
    # must have youtube.com/embed/, add \ before . to let the regex know we want dot(.) not any other character
    
    if matches := re.search(r"<.*https?://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
        return("https://youtu.be/" + matches.group(1))

if __name__ == "__main__":
    main()


# src="https://www.youtube.com/embed/xvFZjo5PgG0" title="Y