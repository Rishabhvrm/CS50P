# extract info
# prompt user for twitter url
# extract user name from that

url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "") # replace starting url with nothing
print(f"Username: {username})

# https://twitter.com/davidjmalan


"""

using replace()

"""