#00
print("stressed"[::-1])

#01
print("".join([y for x, y in enumerate ("パタトクカシー", 1) if x%2==1]))

#02
for x, y in zip ("パトカー", "タクシー"):
    print(x+y, end="")

#03
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(i) for i in text.replace(",", "").replace(".", "").split(" ")])

#04
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ex = [1, 5, 6, 7, 8, 9, 15, 16, 19]
print({x : y[:1] if x in ex else y[:2] for x, y in enumerate(text.replace(",", "").replace(".", "").split(), 1)})

#05
def n_gram (text, n):
    return [text[i:i+n] for i in range(len(text)-n+1)]

print("文字bi-gram:", n_gram("I am an NLPer", 2))
print("単語bi-gram:", n_gram("I am an NLPer".split(" "), 2))

#06
X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))
union_XY = X | Y
intersection_XY = X & Y
difference_XY = X - Y
print("和集合", union_XY)
print("積集合", intersection_XY)
print("差集合", difference_XY)
print("se in X is {0}, se in Y is {1}".format("se" in X, "se" in Y))

#07
def return_text(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)

print(return_text(12, "気温", 22.4))

#08
import re

def cipher(text):
    return "".join([chr(219-ord(i)) if bool(re.match(r"[a-z]", i)) else i for i in text])

print(cipher("abcdef1234"))
print(cipher("zyxwvu1234"))

#09
from random import sample

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
text = text.split(" ")
out = []
for i in text:
    if len(i)<=4:
        out.append(i)
    else:
        out.append(i[0]+"".join(sample(list(i[1:-1]), len(i[1:-1])))+ i[-1])
print(out)