import urllib.request
from urllib.error import HTTPError
import json

URL = "https://www.apache.org/logos/res/logos.json"

with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    for project in data:
         img_url = "https://www.apache.org/logos/res/%s/default.png" % project
         print(img_url)
         try:
             urllib.request.urlretrieve(img_url, filename="%s.png" % project)
         except HTTPError:
             print("Unable to download %s." % img_url)

