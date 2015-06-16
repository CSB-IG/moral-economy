import networkx as nx
import difflib
import pylab as pl
from math import *
from itertools import combinations
import numpy as np
import argparse
###p stands for profile###

parser = argparse.ArgumentParser(description='Creates a network based on agent profile similarities, according to their sequence of characteristics.')
#parser.add_argument('--infile', type=argparse.FileType('r'), required=True)
parser.add_argument('--sim_ratio', type=float, required=True)
args    = parser.parse_args()

g = nx.Graph()

#infile = open( args.infile, 'r' )

#infile = args.infile.read()

infile = [(1,{'p':[2,120000,100,123450,'i0000000',500,1230,0,'i',1,1,1,10000,11,0,000,0,0,1,1,1,100,1,120000]}),(2,{'p':[1,130000,100,123456,12450000,100,1230,1,1,0,1,1,12000,11,0,000,1,0,1,0,0,000,1,127800]}),(3,{'p':[2,130000,100,123456,26000000,100,1230,0,'i',1,0,1,10000,11,0,000,1,1,1,0,0,000,1,239457]}),(4,{'p':[1,100000,100,123456,20000000,200,1230,1,5,0,0,1,10000,11,1,100,1,1,0,1,1,200,1,125800]}),(5,{'p':[2,130000,100,123450,12567000,100,1230,1,2,1,1,1,10000,11,1,123,1,1,0,1,0,000,1,127800]}),(6,{'p':[2,130000,100,123450,12567000,100,1230,1,2,1,1,1,10000,11,1,123,1,1,1,1,0,000,1,127800]}),(7,{'p':[2,130000,100,123450,12500000,100,1230,1,2,0,0,0,10000,11,1,300,0,0,0,0,0,000,0,120000]}),(8,{'p':[2,120000,100,123450,12000000,340,1230,1,3,1,1,0,12300,11,1,100,1,1,1,1,1,100,1,127000]}),(9,{'p':[2,190000,120,134500,12348900,100,1230,1,2,0,0,0,12300,11,1,100,0,0,0,1,0,000,1,127000]}),(10,{'p':[1,141100,123,123456,18000000,100,1230,1,2,'i','i','i',10000,11,0,000,0,0,1,0,0,000,1,120000]}),(11,{'p':[2,100000,100,123460,12456789,200,1230,1,3,1,0,0,10000,10,1,000,1,1,0,1,1,300,1,278000]}),(12,{'p':[1,134000,120,123450,24890000,100,1230,1,1,1,1,1,13000,11,1,460,0,0,0,'i',0,000,1,123790]}),(13,{'p':[1,130000,100,123450,89000000,400,1230,1,5,0,0,0,12340,11,1,600,0,0,0,'i',0,000,1,120000]}),(14,{'p':[1,131011,136,123456,89000000,100,1230,1,5,1,1,1,12345,11,1,600,1,1,0,'i','i',000,1,124700]}),(15,{'p':[1,140000,120,123460,23960000,300,1230,0,'i',1,1,1,12400,11,1,700,1,2,0,1,1,200,1,124700]}),(16,{'p':[1,175600,134,123460,23900000,130,1230,1,1,0,1,1,13400,11,1,200,1,1,0,1,1,123,1,123470]}),(17,{'p':[2,160000,130,123456,23000000,100,1230,1,1,0,1,1,12345,11,0,'i00',0,'i',1,0,0,000,1,147000]}),(18,{'p':[2,100000,100,123460,12348900,300,1200,1,2,1,0,0,10000,11,0,'i00',0,'i',1,0,1,300,1,125400]}),(19,{'p':[2,170000,140,123400,12348900,300,1230,1,1,0,0,0,12000,11,1,700,1,2,0,0,1,130,1,125600]}),(20,{'p':[2,160000,130,123456,20000000,100,1234,1,1,0,1,1,12350,11,1,700,1,2,0,1,1,240,1,127400]}),(21,{'p':[2,100000,100,123460,30000000,400,1200,1,2,1,0,0,10000,11,1,700,0,'i',0,1,1,400,1,127400]}),(22,{'p':[1,146000,123,123456,30000000,300,1230,1,6,0,1,1,13000,11,0,'i00',0,'i',1,1,1,100,1,120000]}),(23,{'p':[2,100000,100,123460,23890000,100,1230,0,'i',0,0,0,10000,10,0,000,0,0,1,1,0,000,1,120000]}),(24,{'p':[2,180000,150,123460,23000000,100,1230,1,4,0,0,0,13000,11,1,200,1,1,0,1,0,000,1,'i00000']}),(25,{'p':[2,140000,120,123450,'i0000000',135,1230,0,'i',0,0,0,10000,11,1,700,0,0,0,'i','i',000,1,700000]}),(26,{'p':[2,150000,130,123460,30000000,100,1230,1,3,1,0,0,12340,11,0,'i00',0,'i',1,1,1,100,1,400000]}),(27,{'p':[1,160000,130,123460,23000000,100,1230,1,1,0,0,1,13400,11,1,250,1,1,0,1,1,200,1,700000]}),(28,{'p':[2,146000,123,123456,20000000,500,1230,1,4,0,0,0,10000,'i',1,1,700,0,'i',1,1,1,100,1,600000]}),(29,{'p':[2,100000,600,123460,15600000,120,1230,1,2,1,0,0,10000,11,1,250,1,1,0,'i',0,123,1,000000]}),(30,{'p':[1,120000,100,123456,'i0000000',200,1230,0,3,0,0,0,10000,11,1,100,1,1,0,0,0,420,1,460000]}),(31,{'p':[1,120000,100,123456,12345890,100,1230,'i',5,1,1,0,12000,'i',1,1,200,1,1,0,0,1,123,1,500000]}),(32,{'p':[2,125000,130,123450,'i0000000',300,1230,1,6,0,0,1,13000,11,1,640,0,'i',0,1,1,000,1,123500]}),(33,{'p':[2,120000,100,123450,'i0000000',340,1200,1,1,0,1,1,13000,11,1,300,0,'i',0,1,0,100,1,460000]}),(34,{'p':[2,125000,130,123450,'i0000000',100,1230,1,2,1,0,0,12000,11,0,000,0,0,1,1,1,200,1,560000]}),(35,{'p':[2,123120,170,123450,12346890,200,1230,1,'i',0,0,0,10000,11,1,700,1,2,0,1,0,100,1,568000]}),(36,{'p':[1,100000,100,123450,12890000,200,1230,1,'i',1,0,1,10000,11,1,100,1,2,0,1,0,123,1,670000]}),(37,{'p':[1,100000,100,123450,24890000,100,1230,1,'i','i','i','i',10000,11,0,000,0,'i',1,1,1,000,1,127000]}),(38,{'p':[2,100000,100,123456,'i0000000',230,1230,1,'i',1,1,0,10000,1,'i',0,000,0,'i',1,1,1,000,1,123500]}),(39,{'p':[2,100000,100,123456,'i0000000',230,1230,1,'i',1,'i',0,10000,11,1,300,1,1,0,1,1,100,1,400000]}),(40,{'p':[2,150000,130,123450,'i0000000',100,1230,1,'i','i','i','i',10000,11,1,460,0,'i',0,0,0,000,1,600000]})]



def creating_weighterd_network():
    g.add_nodes_from( infile )
    for i in g.nodes():
        for j in g.nodes():
            dm = difflib.SequenceMatcher(None, g.node[i]['p'], g.node[j]['p'])
            if dm.ratio() > args.sim_ratio:
                g.add_edge(i,j)
                for i, j in g.edges():
                    g.edge[i][j]['sim'] = dm.ratio()


def edge_weight(g):
    weights = []
    for e in g.edges():
        weights.append(g.get_edge_data(*e)['sim'])

    counts, bins = np.histogram( weights, bins=10 )

    weight = []
    for i,j in g.edges():
        for b in bins:
            if g.edge[i][j]['sim'] >= b:
                weight.append(bins.tolist().index(b)+1)

    return weight


                
def draw():
    nx.draw_networkx_nodes(g, pos = positions,
            node_color = [g.degree(n) for n in nx.nodes(g)],
            #node_size = , #[g.degree(n)**float(3) for n in nx.nodes(g)],
            alpha = 0.7)
            
    nx.draw_networkx_labels(g, pos = positions,fontsize=14)
    nx.draw_networkx_edges(g, pos = positions, 
                  with_labels = True, edge_color = 'c',
                  width = edge_weight(g),
                  cmap = pl.cm.autumn, vmin = 0, vmax = 1)


#creating_network()
creating_weighterd_network()


#positions = nx.circular_layout(g)
positions = nx.spring_layout(g)
#positions = nx.random_layout(g)

draw()
#pl.savefig('55_pc_circular_similarity.png')
pl.show()


#infile =[('E1',{'p':[0,0,5,3,1,0,14,2,6,4,0,4,0,4,26,9,1,0,2,0,5,4,0,1,6,5,1,6,1,4,1,1,0,6,0,4,0,0,2,1,1,1,4,0,1,0,1,10,4,1,0,4,1,0,16,0,4,4,0,10,0,0,2,5,11,0,1,2,1,0,0,12,4,1,18,3,2,1,1,1,1,0,0,3,0,7,80,1,4,0,0,3,4,1,0,0,9,5,2,0,4,3,0,0,3,5,12,4,1,0,0,2,5,1,0,15,0,9,0,0,3]}),('E2',{'p':[0,1,5,4,1,0,6,0,2,5,0,3,0,0,0,0,2,5,0,0,2,0,0,0,0,1,0,0,1,0,1,0,0,3,3,0,0,0,0,1,0,2,0,0,1,0,0,1,0,1,1,1,1,0,8,2,1,2,0,1,0,2,1,1,1,1,1,0,0,0,1,0,2,2,4,1,0,0,0,1,1,0,0,0,0,0,8,0,0,2,0,1,2,1,1,4,1,0,2,0,1,0,0,1,3,0,3,1,0,0,0,2,2,0,1,0,0,1,0,2,0]}),('E3',{'p':[0,0,1,0,1,0,9,1,0,0,1,4,0,3,0,0,1,1,0,0,1,2,1,0,1,7,0,0,2,8,0,3,0,6,0,1,1,0,1,0,5,0,0,1,2,1,0,3,0,2,2,2,2,2,9,1,2,0,0,0,0,0,0,3,0,7,0,0,0,1,0,0,0,0,4,1,1,0,1,0,0,0,0,3,2,1,20,0,0,0,0,0,1,3,0,0,0,0,0,0,2,0,3,0,0,0,6,1,0,0,0,0,2,1,0,4,2,2,1,1,2]}),('E4',{'p':[3,26,18,0,12,0,15,4,11,9,0,2,1,0,0,0,1,0,1,1,20,16,0,7,26,27,0,0,12,10,0,1,1,7,5,10,1,0,1,1,0,1,4,3,0,14,7,16,1,0,0,5,2,1,13,1,8,2,2,0,0,18,1,4,0,0,0,0,0,2,1,0,7,12,17,1,0,0,0,0,13,0,0,4,0,5,139,0,1,1,14,3,3,6,6,25,5,0,0,1,3,0,3,0,4,5,2,0,8,0,5,1,3,6,0,1,2,6,2,2,6]}),('E5',{'p':[1,0,3,0,2,2,3,3,2,1,0,1,0,0,0,0,2,2,0,0,0,1,0,0,2,11,1,1,6,3,0,6,3,3,0,0,0,0,1,0,0,0,0,0,0,0,1,2,1,2,2,4,2,0,11,0,1,3,3,0,0,1,0,4,0,0,0,0,0,0,0,0,0,3,5,1,0,5,2,0,3,0,0,0,1,4,22,0,3,11,1,0,1,1,0,4,0,0,0,0,2,0,0,0,3,0,6,2,0,0,0,3,1,1,0,1,0,2,1,2,0]}),('E6',{'p':[0,0,1,0,0,0,7,4,0,0,0,0,1,3,0,0,0,0,0,0,0,3,0,1,3,3,0,0,0,0,0,3,3,14,0,0,0,0,0,0,1,0,0,0,0,0,0,3,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,1,0,2,0,0,11,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,37,9,0,0,1,0,0,0,0,2,3,1,0,0,0,0,0,0,0,2,1,2,0,0,0,1,0,1,0,0,0,1,0,0,0]}),('E7',{'p':[9,1,3,2,0,2,45,17,13,15,0,11,11,5,11,2,2,4,5,7,4,5,0,9,53,8,3,0,2,14,0,0,0,26,8,3,0,16,1,6,3,1,33,3,1,8,2,13,9,5,4,9,1,6,36,2,4,13,3,1,17,11,4,5,2,7,9,4,3,4,7,6,4,9,6,4,3,0,0,6,3,29,9,3,4,21,105,0,12,0,8,5,22,9,0,23,12,9,8,10,2,0,0,13,3,2,13,17,1,12,1,3,15,1,6,11,0,10,4,6,16]}),('E8',{'p':[3,2,7,2,3,0,2,5,3,6,0,1,2,0,2,5,1,7,0,0,0,4,3,0,2,15,0,0,0,8,0,11,2,7,8,2,10,0,2,0,0,4,0,0,7,1,0,8,3,1,2,6,1,0,5,5,1,7,1,0,0,7,1,11,0,0,1,0,0,0,1,0,0,2,25,3,0,2,4,1,1,0,0,8,0,1,36,1,0,1,1,2,0,1,0,7,11,0,1,0,14,3,0,1,2,2,14,1,0,0,1,1,3,1,1,1,0,1,2,0,4]}),('E9',{'p':[1,1,6,2,0,0,4,6,1,5,0,0,5,1,1,0,0,4,0,0,0,0,0,1,6,8,1,0,9,12,0,2,0,5,5,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,0,2,0,4,2,0,1,0,4,0,0,4,0,1,2,0,0,0,0,0,5,8,0,2,1,0,0,1,0,0,2,1,4,32,0,0,4,0,1,0,0,0,0,2,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,3,0,0,1,1,0]}),('E10',{'p':[1,1,4,2,0,3,17,5,0,2,0,5,0,2,9,0,1,0,0,0,0,0,3,0,0,19,10,0,0,10,4,0,0,17,0,0,0,0,3,3,0,3,4,0,1,8,0,3,9,0,0,0,3,2,29,0,6,0,0,3,0,1,0,7,0,2,0,3,0,0,2,0,0,1,6,2,1,4,0,4,9,0,2,1,0,13,30,2,4,0,1,1,0,8,1,0,4,1,2,0,1,0,2,0,4,1,6,3,0,0,0,2,4,1,2,3,1,6,1,0,2]}),('E11',{'p':[1,1,0,0,0,0,2,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,5,0,1,2,3,0,1,3,3,0,0,9,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,3,0,1,0,1,1,0,3,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,2,5,0,0,2,0,4,0,3,2,0,2,1,1,0,8,0,0,0,3,0,1,0,0,0,1,2,1,0,0,1,2,1,1,0,2]}),('E12',{'p':[0,1,1,2,1,1,39,5,0,2,0,2,9,0,0,0,1,0,1,0,5,3,3,0,0,6,0,0,2,3,1,0,6,2,0,0,0,0,0,2,1,0,0,0,1,0,2,0,4,1,0,5,0,0,18,0,9,2,2,1,1,0,1,5,0,1,0,2,0,1,1,0,0,0,10,2,0,2,0,0,2,1,0,0,0,4,34,0,2,1,1,6,0,0,1,0,1,2,0,0,3,0,0,1,4,0,2,5,0,0,0,2,9,1,3,6,0,3,0,4,4]}),('E13',{'p':[0,4,2,0,0,6,6,1,0,10,0,0,1,2,0,0,0,0,0,2,1,0,0,0,0,1,2,5,3,1,0,18,0,1,0,0,0,2,1,10,0,0,1,0,0,2,0,2,1,0,0,0,3,1,2,1,0,0,0,0,0,0,0,3,0,1,0,1,0,3,0,0,0,0,1,2,0,0,0,4,0,0,0,1,1,2,16,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,3,0,4,0,1,1,2,2,0,0,1]}),('E14',{'p':[0,0,0,0,1,0,1,2,0,19,5,0,2,0,0,0,0,0,0,0,2,1,0,0,0,3,0,2,1,1,0,1,2,1,4,0,2,0,1,0,0,0,0,1,0,1,3,1,11,0,1,0,1,1,2,0,0,1,0,0,1,2,8,4,0,0,0,1,0,1,0,0,0,1,10,3,0,0,0,0,1,0,0,0,0,2,17,0,1,0,0,2,1,1,2,0,15,4,0,0,2,0,0,0,2,0,0,3,0,0,1,0,3,4,0,3,0,1,0,2,2]}),('E15',{'p':[0,1,1,1,2,1,5,2,0,0,5,0,0,2,0,0,0,0,0,0,0,0,1,0,0,7,0,0,0,1,1,0,0,4,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,6,2,0,1,1,0,0,0,0,0,1,0,2,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,2,8,0,0,0,0,3,0,0,0,0,0,2,0,0,0,7,1,0,0,0,0,2,0,1,0,1,2,0,1,5,2,0,0,0,0]}),('E16',{'p':[1,0,2,0,0,1,7,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,6,0,0,0,2,0,2,0,2,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,2,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,4,11,0,0,0,0,0,0,0,0,1,0,0,2,0,2,4,0,0,0,0,0,3,0,0,1,0,2,0,0,5,1,0,0,0,1]}),('E17',{'p':[1,0,6,0,2,0,2,1,0,10,0,0,0,0,0,0,0,0,3,11,0,0,1,0,0,4,0,1,0,1,4,0,2,1,0,0,0,0,0,0,0,0,1,0,6,1,0,3,0,0,2,5,1,2,5,0,0,0,4,0,0,0,0,2,0,0,0,0,0,0,0,0,0,3,22,2,0,2,14,2,0,0,0,0,2,0,14,0,0,6,1,2,0,1,0,3,1,0,0,0,17,0,0,0,0,3,1,0,1,0,0,0,4,0,1,5,1,0,0,0,0]}),('E18',{'p':[2,2,13,0,3,0,23,0,1,19,16,1,17,9,4,0,1,0,6,0,8,2,5,0,4,7,0,1,2,7,0,0,1,8,6,7,6,0,3,5,3,3,0,5,3,0,1,1,1,3,1,2,1,5,24,3,8,3,0,0,3,5,7,5,1,5,1,1,0,1,0,6,1,3,21,2,4,7,0,1,2,3,4,1,2,9,35,3,18,2,15,20,8,20,1,3,12,0,0,2,14,0,4,6,1,1,21,4,3,2,5,0,5,2,0,11,3,8,2,2,59]}),('E19',{'p':[1,1,1,1,0,3,8,0,0,8,4,0,0,1,2,0,0,0,0,0,0,0,0,0,1,1,0,0,0,11,1,0,0,8,0,0,0,0,0,5,0,1,15,1,2,0,0,0,10,0,0,2,3,2,11,0,0,0,1,1,0,2,2,0,0,0,0,1,0,2,1,0,0,0,2,1,2,2,2,0,7,1,0,0,2,6,18,0,0,0,0,1,0,2,0,0,5,2,0,0,1,0,9,0,0,2,0,2,1,0,0,1,2,1,1,2,4,1,3,1,2]})]
