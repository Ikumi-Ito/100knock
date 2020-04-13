import json
import gzip
import re

def open():
    with gzip.open("jawiki-country.json.gz") as file:
        for i in file:
            j = json.loads(i)
            if j["title"] == "イギリス":
                return j["text"]

text = open()
for i in text.split("\n"):
    line = re.findall("^\[{2}Category:(.*?)(|\|.*)\]{2}$", i)
    if line is not None:
        print(line.group(1))