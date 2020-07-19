file = open("MST.txt")

graph = [[] for i in range(0,501)]

for i,line in enumerate(file):
    u, v, weight = [int(x) for x in line.split()]
    graph[u].append([v,weight])
    graph[v].append([u,weight])

file.close()

X = [1]
cost = 0

while len(X) < 500:
    min_weight = 10000000000
    min_v = -1
    min_w = -1
    
    for v in X:
        edges = graph[v]
        for edge in edges:
            if edge[1] < min_weight and edge[0] not in X:
                min_weight = edge[1]
                min_v = v
                min_w = edge[0]
    
    X.append(min_w)
    
    cost += min_weight
    
print(cost)
