from no41 import dependency_analysis

dependency = dependency_analysis('neko.txt.cabocha')

with open('result_no47', 'w') as file:
    for one_line in dependency:
        for number, phrase in enumerate(one_line):     
            #「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る文節を格納するリストを定義
            function_verb_syntax = []
            #動詞を持つオブジェクトに対して処理を行う
            if phrase.pos_in_or_no('動詞'):
                for word in phrase.morphs:
                    if word.pos == '動詞' and one_line[number-1].morphs[-1].surface == "を" and one_line[number-1].morphs[0].pos1 == 'サ変接続':
                        specified_lause = []
                        #それぞれの単語を順にしてリストに格納する
                        specified_lause.extend([one_line[number-1].morphs[0].surface, 'を', word.base])
                        #構文化してリストに追加する
                        function_verb_syntax.append(''.join(specified_lause))
            if function_verb_syntax == []:
                continue
            
            #助詞と文節のタプルを格納するリストを定義する
            pos_phrase_list = []
            
            #係り元のインデックスを取得する
            for index in phrase.srcs:
                #品詞に助詞を持つ係り元のオブジェクトに対して処理を行う
                if one_line[index].pos_in_or_no('助詞'):
                    #係り元の単語を一つずつ順に取り出す
                    for word in one_line[index].morphs:
                        if word.pos == '助詞' and not one_line[index].making_phrase() in function_verb_syntax[0]:
                            #助詞と、その助詞を含む文節のタプルを、リストに格納する
                            pos_phrase_list.append((word.surface, one_line[index].making_phrase()))
                else:
                    continue
                
            if function_verb_syntax != [] and pos_phrase_list != []:
                #助詞を元にして、あいうえお順にソートする
                pos_phrase_list.sort(key=lambda x: x[0])
                #ファイルに書き込む
                file.write('{}\t{}\t{}\n'.format(function_verb_syntax[0],\
                                                  ' '.join([x[0] for x in pos_phrase_list]),\
                                                   ' '.join(x[1] for x in pos_phrase_list)))