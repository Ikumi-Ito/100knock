from no41 import dependency_analysis


dependency = dependency_analysis('neko.txt.cabocha')
out = []
one_line = []
for morphs_out in dependency[:10]:
    for morph_out in morphs_out:
        #文節と品詞の二次元配列を作る
        a = morph_out.phrase_and_poslist()
        #一文ごとにリストに一時保管
        one_line.append(a)
    #一文ごとに一時保管していたリストをoutリストに追加
    out.append(one_line)
    one_line = []

for phrases in out:
    for phrase in phrases:
        #係り先のインデックス番号を取得
        index = phrase[-1][-1]
        if '名詞' in phrase[-1] and '動詞' in phrases[index][-1] and index != -1:
            print('{}\t{}'.format(phrase[0], phrases[index][0]))