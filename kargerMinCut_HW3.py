import math
import copy
import numpy as np
import random


def edge_contra(graph,nodeA,nodeB):
    graph[nodeA] = graph[nodeA] + graph[nodeB]
    graph.pop(nodeB)
    for i in graph:
        for j in range(len(graph[i])):
            if graph[i][j] == nodeB:
                graph[i][j] = nodeA
    #remove the self loop
    graph[nodeA] = filter(lambda x: x != nodeA, graph[nodeA])
    
    return graph

def min_cut(graph):
    if(len(graph) == 2): 
        return len(graph.values()[0])
    else:
        nodeA = random.choice(graph.keys())
        nodeB = random.choice(graph[nodeA])
        graph = edge_contra(graph, nodeA, nodeB)
        min_cut(graph)
        return len(graph.values()[0])




if __name__=="__main__":
    f = open("./kargerMinCut.txt","r")
    graph = {}
    for l in f.readlines():
        dic = list(map(int,l.split()))
        graph[dic.pop(0)] = dic
    f.close()
    
    i = 0
    length = len(graph)
    mincuts = length**2
    #make sure you understand why you should use the deepcopy here!!!
    #important!!!!
    while i < length**2*math.log(length):
        new_graph = copy.deepcopy(graph)
        newMincut = min_cut(new_graph)
        if newMincut < mincuts:
            mincuts = newMincut
            print mincuts
        i += 1
