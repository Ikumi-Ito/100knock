from no41 import dependency_analysis

dependency = dependency_analysis('neko.txt.cabocha')

def relation_phrase_pos(dependency):
    out_list = []
    one_line = []
    for morphs_out in dependency:
        for morph_out in morphs_out:
            a = morph_out.basephraselist_and_poslist()
            one_line.append(a)
        out_list.append(one_line)
        one_line = []

    return out_list

biggest = relation_phrase_pos(dependency)
with open('result_no45', 'w') as file:
    for phrases in biggest:
        if phrases != []:
            out = {}
            particles_list = []
            one_particle = []
            for phrase in phrases:
                index = phrase[-1][-1]
                if '助詞' in phrase[-1] and '動詞' in phrases[index][-1] and index != -1:
                    verb_index = phrases[index][-1].index('動詞')
                    particle_index = phrase[-1].index('助詞')
                    verb = phrases[index][0][verb_index]
                    particle = phrase[0][particle_index]
                    if not verb in out:
                        one_particle.append(particle)
                        out[verb] = one_particle
                        one_particle = []
                    elif verb in out:
                        particles_list = out[verb]
                        particles_list.append(particle)
                        out[verb] = particles_list
                        particles_list = []
        
            if out != {}:
                for verb, pos in out.items():
                    file.write('{}\t{}\n'.format(verb, ' '.join(pos)))