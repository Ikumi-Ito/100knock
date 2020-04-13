from no30 import Morphological＿analysis

morpheme_list = Morphological＿analysis('neko.txt')
out = []
for sentence in morpheme_list:  #一文ずつのリストを順に取り出す
    for word in sentence:   #一文ずつのリストから各単語ごとの形態素解析結果を順に取り出す
        if word['pos'] == '動詞':   #品詞が動詞である単語に処理を限定する
            out.append(word['base'])    #動詞の原型を抽出する
print(out[:10])