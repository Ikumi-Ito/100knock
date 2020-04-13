from no30 import Morphological＿analysis
from no36 import Count_order
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import Counter

morpheme_list = Morphological＿analysis('neko.txt')
counting_order = Count_order(morpheme_list)

x = []

for word_number in counting_order:
    x.append(word_number[1])    #各単語の出現頻度を抽出する。

counting = Counter(x)
counting = counting.most_common()   #[単語の頻度]:[個数]のタプルを生成する

xdata = []
ydata = []

for index, i in enumerate(counting, 1):
    xdata.append(index)     #順位を順にx軸用のリストに格納
    ydata.append(i[1])      #各単語の出現回数をy軸用のリストに格納

plt.scatter(xdata, ydata)
plt.xscale('log')
plt.yscale('log')

plt.savefig('log.png')