from heapq import heappop, heappush

f = open("./dijkstraData.txt", "r")
graph = {}

for l in f.readlines():
    #print int(l.split()[0]), map(int,l.split()[1].split(','))
    
    data = l.split()
    node1 = int(data[0])-1
    for input_num in data[1:]:
        node2, weight = map(int,input_num.split(','))
        temp = {}
        node2 -= 1
        temp[node2] = weight
        if node1 in graph.keys():
            graph[node1].update(temp)
        else:
            graph[node1] = temp


def dij_short_path(graph, s):
    infi = 10000
    weights = [infi] * (len(graph))
    weights[s] = 0
    n  = len(graph)
    Q = [(0,s)]
    visited = [False] * (len(graph))
    
    while len(Q) > 0:
        (cost, u) = heappop(Q)
        if visited[u]:
            continue
        else:
            visited[u] = True
        
            for v in graph[u]:
                weights[v] = min(weights[v], weights[u]+ graph[u][v])
                heappush(Q, (weights[v], v))

        
    return weights



ans = dij_short_path(graph, 0)


lis= [7,37,59,82,99,115,133,165,188,197]

res = [ans[i-1] for i in lis]

print res


