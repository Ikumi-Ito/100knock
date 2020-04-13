import json
import gzip

def open1():
    with gzip.open("jawiki-country.json.gz", "rt") as file:
        for i in file:
            j = json.loads(i)
            if j["title"] == "イギリス":
                return j["text"]

text = open()
for i in text.split("\n"):
    if "Category" in i:
        print(i)