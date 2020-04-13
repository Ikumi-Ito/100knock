import json
import gzip

with gzip.open("jawiki-country.json.gz", "rt") as file:
    for i in file:
        j = json.loads(i)
        if j["title"] == "イギリス":
            print (j["text"])
            break