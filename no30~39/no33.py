from no30 import Morphological＿analysis

morpheme_list = Morphological＿analysis('neko.txt')
out = []
for sentence in morpheme_list:
    for word in sentence:
        if word['pos1'] == 'サ変接続' and word['pos'] == '名詞':    #品詞がサ変接続かつ名詞である単語に処理を限定する
            out.append(word['base'])
print(out[:10])