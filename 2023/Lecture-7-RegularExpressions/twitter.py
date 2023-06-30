# extract info
# prompt user for twitter url
# extract user name from that

import re

url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "") # replace starting url with nothing
# username = url.removeprefix("https://twitter.com/")

# substitute
re.sub(r"https://twitter.com/", "", url)

print(f"Username: {username}")

# https://twitter.com/davidjmalan


"""

using string methods
    replace()
    removeprefix()

using re method
    re.sub(pattern, repl, string, count=0, flags=0)     # substitue, replacement
"""