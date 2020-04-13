import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __repr__(self):
        return 'surface : {}, base : {}, pos : {}, pos1 : {}'.format(self.surface, self.base, self.pos, self.pos1)

def morph(file):
    with open(file, 'r') as f:
        text = f.readlines()
    out = []
    one_line = []
    for line in text:
        if line[0] == '*':  #係り受け解析の結果を無視する
            continue
        elif line == 'EOS\n':
            out.append(one_line)  #一文ごとにone_lineに格納する
            one_line = []  #one_lineを空のリストで上書きし、一文区切りの二次元配列を作る
        else:
            surface = line.split('\t')[0]
            others_list = re.split('\t|,', line)  #\tと,で形態素解析結果を分割する
            one_line.append(Morph(surface, others_list[7], others_list[1], others_list[2]))

    return out

if __name__ == '__main__':
    from pprint import pprint
    out = morph('neko.txt.cabocha')
    for number, morph_out in enumerate(out, 1):
        if number == 3:
            pprint(morph_out)