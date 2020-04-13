from no30 import Morphological＿analysis

morpheme_list = Morphological＿analysis('neko.txt')
out = []

for sentence in morpheme_list:
    for index in range(len(sentence)-1):
        special_index = index + 1
        while special_index <= len(sentence)-1:
            if sentence[index]['pos'] == '名詞' and sentence[special_index]['pos'] == '名詞':   #名詞の連結が続く部分のindexを調べる
                special_index += 1
                continue
            else:
                break   #名詞の連結が終わったら処理をやめる
        if special_index-index>=2:      #2単語以上名詞が連結していたら処理を行う
            special_out = sentence[index:special_index]     #一文の中から、名詞が連結している部分のマップを抽出する
            word = []
            for i in range(len(special_out)):
                word.append(special_out[i]['surface'])      #各マップから取り出した単語でリストを作る
            out.append(''.join(word))   #要素を連結させて最長一致の名詞の連続を一つの要素としてoutに追加

print(out[:10])