import networkx as nx

# brain = brain=nx.Dibrainraph() #for the first time
brain = nx.read_edgelist('db.edgelist', create_using=nx.Dibrainraph(), nodetype=str, data=(('weight', int),)) 


def simple_learn(brain):
    while True:
        s = input()
        if s == 'quit':
            return
        else:
            ind = s.find(' ')
            inp_edge = (s[:ind], s[ind + 1:])
            if inp_edge in brain.edges():
            	brain.edge[s[:ind]][s[ind + 1:]]['weight'] += 1
            else:
            	brain.add_edges_from([inp_edge], weight = 1)
            nx.write_edgelist(brain,'db.edgelist',data=['weight'])

simple_learn(brain)

