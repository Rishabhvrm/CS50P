# APIs - third party services that we can write code to talk to
# act like a browser and download data

# requests package to make api web requests

# JSON - language agnostic

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2))