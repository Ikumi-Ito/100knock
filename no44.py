from graphviz import Digraph
from no41 import dependency_analysis
from no42 import making_relation

dependency = dependency_analysis('neko.txt.cabocha')
phrases = making_relation(dependency)

def making_tree(phrases_list):
    dg = Digraph(format='png')
    for two_phrases in phrases_list:
        origin = two_phrases[0]
        destination = two_phrases[1]
        dg.attr('node', shape='circle', color='dodgerblue')
        dg.attr('edge', color='dodgerblue')
        dg.node(origin, style='filled', fillcolor='darkslategray1')
        dg.node(destination, style='filled', fillcolor='darkslategray1')
        dg.edge(origin, destination)
    dg.render('treegraph_no44', view=True)

making_tree(phrases[6])