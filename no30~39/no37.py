
from no30 import Morphological＿analysis
from no36 import Count_order
import matplotlib.pyplot as plt
import japanize_matplotlib

morpheme_list = Morphological＿analysis('neko.txt')
counting_order = Count_order(morpheme_list)

left = []
height = []
label = []

for index, word_number in enumerate(counting_order[:10], 1):
    left.append(index)
    height.append(word_number[1])
    label.append(word_number[0])

fig = plt.figure()      #Figureインスタンスを生成する。壁画全体の領域を確保する。
ax = fig.add_subplot(1, 1, 1)       #確保した領域に区切りを付ける。今回は1,1,1なので一画面に一個のグラフ
ax.bar(left, height, tick_label = label, align = 'center')
ax.set_xlabel('文字')
ax.set_ylabel('回数')

plt.savefig('bar.png')