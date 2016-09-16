# -*- coding: utf-8 -*- 
import networkx as nx

# brain = nx.DiGraph() #for the first time
brain = nx.read_edgelist('database.edgelist', create_using = nx.DiGraph(), nodetype=str, data=(('weight', int),)) 

# def ask(brain):
#     print "Что ты хочешь спросить у меня?"
    
# ask(brain):





# def simple_learn(G):
#     while True:
#         s = input()
#         if s == 'quit':
#             return
#         else:
#             ind = s.find(' ')
#             inp_edge = (s[:ind], s[ind + 1:])
#             if inp_edge in G.edges():
#                 G.edge[s[:ind]][s[ind + 1:]]['weight'] += 1
#             else:
#                 G.add_edges_from([inp_edge], weight = 1)
#             nx.write_edgelist(G,'db.edgelist',data=['weight'])

# simple_learn(DG)

