def find(u):
    while u != sets[u]:
        u = sets[u]
    return u

nodes = 500
k = 4
sets = [i for i in range(0,nodes+1)]
edges = []

file = open("Clusters.txt")

for i,line in enumerate(file):
    u, v, weight = [int(x) for x in line.split()]
    edges.append([u,v,weight])

file.close()

edges = sorted(edges, key=lambda x: x[2])

vertices = 0
i = 0

while vertices < nodes-k+1:
    u, v, weight = edges[i]
    
    i += 1
    
    if find(u) == find(v):
        continue
        
    sets[find(u)] = find(v)
    
    vertices += 1

print(edges[i-1][2])
    