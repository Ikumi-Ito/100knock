from no30 import Morphological＿analysis
from no36 import Count_order
import matplotlib.pyplot as plt
import japanize_matplotlib

morpheme_list = Morphological＿analysis('neko.txt')
counting_order = Count_order(morpheme_list)

x = []

for word_number in counting_order:
    x.append(word_number[1])    #各単語の出現回数の数字を抽出してリストに格納する

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(x, bins=30 ,range=(1, 30), rwidth=0.6)
ax.set_xlabel('回数')
ax.set_ylabel('個数')

plt.savefig('hist.png')