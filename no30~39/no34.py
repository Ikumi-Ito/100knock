from no30 import Morphological＿analysis
from pprint import pprint

morpheme_list = Morphological＿analysis('neko.txt')


out = []

for sentence in morpheme_list:
    for index in range(len(sentence) - 1):
        if sentence[index]['surface'] == 'の' and \
            sentence[index-1]['pos'] == '名詞' and \
            sentence[index+1]['pos'] == '名詞':     #「の」の前後が名詞である部分を検索する
            out.append(sentence[index-1]['surface'] + sentence[index]['surface'] +sentence[index+1]['surface'])     #「の」を含めた3つの形態素を抽出する

print(out[:10])