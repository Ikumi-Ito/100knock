import gzip
import json
import re

def open():
    with gzip.open("jawiki-country.json.gz", "rt") as file:
        for i in file:
            j = json.loads(i)
            if j["title"] == "イギリス":
                return j["text"]

text = open()
for i in text.split("\n"):
    out = re.search("(={2,5})\s*(.*?)\s*={2,5}", i)
    if out is not None:
        print(out.group(2), (out.group(1).count("="))-1)