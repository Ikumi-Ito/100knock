from no41 import dependency_analysis

dependency = dependency_analysis('neko.txt.cabocha')

with open('result_no46', 'w') as file:
    for one_line in dependency:
        for phrase in one_line:
            
            #動詞の原型を格納するリストを定義
            baseverb_list = []
            #動詞を持つオブジェクトに対して処理を行う
            if phrase.pos_in_or_no('動詞'):
                for word in phrase.morphs:
                    if word.pos == '動詞':
                        #品詞が動詞である単語をリストに追加する
                        baseverb_list.append(word.base)
            else:
                continue
            
            #助詞と文節をのタプルを格納するリストを定義する
            pos_phrase_list = []
            
            #係り元のインデックスを取得する
            for index in phrase.srcs:
                #品詞に助詞を持つ係り元のオブジェクトに対して処理を行う
                if one_line[index].pos_in_or_no('助詞'):
                    #係り元の単語を一つずつ順に取り出す
                    for word in one_line[index].morphs:
                        if word.pos == '助詞':
                            #助詞と、その助詞を含む文節のタプルを、リストに格納する
                            pos_phrase_list.append((word.surface, one_line[index].making_phrase()))
                            
                else:
                    continue
            
            if pos_phrase_list != []:
                pos_phrase_list.sort(key=lambda x: x[0])
                file.write('{}\t{}\t{}\n'.format(baseverb_list[0],\
                                                  ' '.join([x[0] for x in pos_phrase_list]),\
                                                   ' '.join(x[1] for x in pos_phrase_list)))