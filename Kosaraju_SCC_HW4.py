import sys
import threading


def readDirectedGraph(filename):
    f = open(filename)

    adjlist = []
    adjlist_reversed = []

    line = f.readline()
    while line != '':
        num1, num2 = line.split()
        v_from = int(num1)
        v_to = int(num2)
        max_v = max(v_from, v_to)

        while len(adjlist) < max_v:
            adjlist.append([])
        while len(adjlist_reversed) < max_v:
            adjlist_reversed.append([])

        adjlist[v_from-1].append(v_to-1)
        adjlist_reversed[v_to-1].append(v_from-1)

        line = f.readline()

    return adjlist, adjlist_reversed



def dfs_1(graph_rev, i):
    global ftime, t, visited
    visited[i] = True
    for vertex in graph_rev[i]:
        if not visited[vertex]:
            dfs_1(graph_rev, vertex)
    ftime[t] = i
    t += 1


def dfs_loop_1(graph_rev, n):
    global visited, t, ftime
    t = 0
    visited = [False]*n
    ftime = [None]*n
    for i in reversed(range(n)):
        if not visited[i]:
            dfs_1(graph_rev,i)


def dfs_2(graph, i):
    global visited, scc_size
    visited[i] = True
    for vertex in graph[i]:
        if not visited[vertex]:
            dfs_2(graph, vertex)
    scc_size += 1

def dfs_loop_2(graph, n):
    global visited, scc_size, ftime
    visited = [False] * n
    result = []
    for i in reversed(range(len(graph))):
        if not visited[ftime[i]]:
            scc_size = 0
            dfs_2(graph, ftime[i])
            result.append(scc_size)

    return result



def kosarajuSCC(graph, graph_rev):
    n = len(graph)
    dfs_loop_1(graph_rev, n)
    res = dfs_loop_2(graph, n)

    return res

def loadgraph():
    f = open("./SCC.txt", "r")
    graph = {}
    for l in f.readlines():
        dic,vertex = list(map(int,l.split()))[0], list(map(int,l.split()))[1]
        if dic not in graph.keys():
            graph[dic] = [vertex]
        else:
            graph[dic] += [vertex]
    f.close()

    return graph


def main():
    print "start"

    #graph = loadgraph()
    graph, graph_rev = readDirectedGraph('SCC.txt')
    print "Finished loading graph"
    #graph_rev = reverse_graph(graph)
    #print "Finished reversing graph"
    print "\n"
    print "Now calcluating the scc size"
    res = kosarajuSCC(graph, graph_rev)
    print "Calculating done:\n"
    print(','.join(map(lambda x: str(x), sorted(res)[::-1][:5])))


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()
