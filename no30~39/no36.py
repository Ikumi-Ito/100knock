from no30 import Morphological＿analysis
from collections import Counter

morpheme_list = Morphological＿analysis('neko.txt')

def Count_order(morpheme_list):
    morpheme_list = morpheme_list[1:]
    word_list = []

    for sentence in morpheme_list:
        for index in range(len(sentence)):
            word_list.append(sentence[index]['surface'])    #表層形のみ抽出しword_listに格納する

    counting = Counter(word_list)   #各単語の出現回数を数える
    counting_order = counting.most_common()     #出現回数の多い順に並び替え
    
    return counting_order

if __name__ == '__main__':      #これ以降の部分は外部ファイルからimportされた時に実行されない。このファイルを直接実行した場合のみ、処理が行われる
    from pprint import pprint
    out = Count_order(morpheme_list)
    pprint(out[:10])