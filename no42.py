from no41 import dependency_analysis

dependency = dependency_analysis('neko.txt.cabocha')
for morphs_out in dependency[:10]:
        for morph_out in morphs_out:
            if morph_out.dst != -1:
                origin = morph_out.making_phrase()
                origin = origin.rstrip('、')
                destination = morphs_out[morph_out.dst].making_phrase()
                destination = destination.rstrip('。').rstrip('、')
                print('{}\t{}'.format(origin, destination))