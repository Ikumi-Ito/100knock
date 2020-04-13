from no30 import Morphological＿analysis

morpheme_list = Morphological＿analysis('neko.txt')
out = []
for sentence in morpheme_list:  #一文ごとのリストを順に取り出す
    for word in sentence:   #一文ごとのリストから各単語ごとの形態素解析結果を取り出す
        if word['pos'] == '動詞':   #品詞が動詞である単語を抽出する
            out.append(word['surface'])
print(out[:10])