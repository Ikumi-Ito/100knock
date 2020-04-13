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
text = re.findall("\{{2}基礎情報(.*?)\}{2}$", text, re.MULTILINE + re.DOTALL)
print(text)
text = re.findall("^\|(.*?)\s=\s(.*?)(?=\n)(?!\n\*)", text[0], re.MULTILINE + re.DOTALL)
print(text)
for x, y in dict(text).items():
    print(x, y)