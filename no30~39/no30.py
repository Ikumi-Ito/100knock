import MeCab
import re


def Morphological＿analysis(file):
    with open(file, 'r') as f:
        text = f.readlines()
    processed_text = [i for i in text if not re.match('\n', i)]  #文と文の間の改行を取り除く
    m = MeCab.Tagger('-Ochasen')
    out = []
    for line in processed_text:
        morpheme = m.parseToNode(line)
        one_line = []   #一文ずつ格納するリストを定義する
        while morpheme:
            word = {}
            feature = morpheme.feature.split(',')
            if feature[0] != 'BOS/EOS':     #形態素解析の最初と最後の一行を除外する
                word['surface'] = morpheme.surface
                word['base'] = feature[6]
                word['pos'] = feature[0]
                word['pos1'] = feature[1]
                one_line.append(word)   #各単語ごとの形態素解析済みの辞書を、一文用のリストに格納する
            morpheme = morpheme.next
        out.append(one_line)    #一文全ての形態素が入ったリストを、提出用リストに格納する
    
    return out


if __name__ == '__main__':      #これ以降の部分は外部ファイルからimportされた時に実行されない。このファイルを直接実行した場合のみ、処理が行われる
    from pprint import pprint
    out = Morphological＿analysis('neko.txt')
    pprint(out[:5])