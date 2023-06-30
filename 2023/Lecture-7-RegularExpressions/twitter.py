# extract info
# prompt user for twitter url
# extract user name from that

import re

url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "") # replace starting url with nothing
# username = url.removeprefix("https://twitter.com/")

# substitute
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# (.+) is for return value, we used (www.) for grouping but it also returns a value
# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):  print(f"Username:", matches.group(1))
# only take data that is needed, we don't need www in above
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):     # here we specify that we don't need www. therefore it will not return its value and we can get the value in matches.group(1) instead of matches.group(2)
    print(f"Username:", matches.group(1)) # not matches.group(2) now because of (?:www\.)

# https://twitter.com/davidjmalan


"""
Notes:

using string methods
    replace()
    removeprefix()

using re method
    re.sub(pattern, repl, string, count=0, flags=0)     # substitue, replacement
    re.search()
    re.split(pattern, string, maxsplit=0, flags=0)      # split string using multiple chars
    re.findall(pattern, string, flags=0)                # multiple copies of same pattern in string

"""