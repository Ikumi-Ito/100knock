import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __repr__(self):
        return 'surface : {}, base : {}, pos : {}, pos1 : {}'\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def making_phrase(self):
        return  ''.join([morph.surface for morph in self.morphs])


def dependency_analysis(file):
    with open(file, 'r') as f:
        text = f.readlines()

    #返り値用のリスト
    out = []
    #一文ずつのまとまりを作るためのリスト
    one_line = []

    for line in text:
        #係り受け解析の部分の処理
        if line[0] == '*':
            line = line.split(' ')
            #Chunkオブジェクトを作る
            dependency = Chunk(int(line[2].strip('D')))
            one_line.append(dependency)

        #一文が終わったときの処理
        elif line == 'EOS\n':
            for number, obj in enumerate(one_line):
                #係り先がある場合に、係り元のインデックス番号を係り先のメンバ変数srcsに追加する
                if obj.dst != -1:
                    one_line[obj.dst].srcs.append(number)
            out.append(one_line)
            #one_lineを空のリストで上書きし、一文区切りの二次元配列を作る
            one_line = []

        #形態素解析の部分の処理
        else:
            surface = line.split('\t')[0]
            others_list = re.split('\t|,', line)
            #Morphオブジェクトを作る
            morphs = Morph(surface, others_list[7], others_list[1], others_list[2])
            #インスタンスオブジェクトdependencyのメンバ変数morphsに、インスタンスオブジェクトmorphsを追加
            dependency.morphs.append(morphs)

    return out


if __name__ == '__main__':
    from pprint import pprint
    out = dependency_analysis('neko.txt.cabocha')
    for number, morphs_out in enumerate(out, 1):
        if number == 8:
            for index, morph_out in enumerate(morphs_out):
                pprint('({}){}  :{}'.format(index, morph_out.making_phrase(), morph_out.dst))