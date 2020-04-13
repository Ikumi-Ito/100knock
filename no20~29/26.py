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
out = re.search("\{{2}基礎情報(.*?)\}{2}$", text, re.MULTILINE + re.DOTALL)
if out is not None:
    print(out.group(1))