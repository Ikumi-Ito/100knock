import json
import gzip
import re

def open():
    with gzip.open("jawiki-country.json.gz", "rt") as file:
        for i in file:
            j = json.loads(i)
            if j["title"] == "イギリス":
                return j["text"]

text = open()
for i in text.split("\n"):
    out = re.search("(ファイル|File):(.*?)\|", i, re.MULTILINE + re.DOTALL)
    if out is not None:
        print(out.group(2))