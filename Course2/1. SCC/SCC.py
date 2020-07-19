from tqdm import tqdm

def DFS(graph, i, inverted):
    global t
    global s
    
    stack = [i]
    
    while len(stack): 
        x = stack[-1]
            
        explored[x] = 1
        leader[x] = s
        
        recursed = False
        
        for edge in graph[x]:
            if not explored[edge]:
                stack.append(edge)
                recursed = True
        
        if not recursed: 
            
            if inverted and not processed[x]:
                t += 1
                fin_times[t] = x
                processed[x] = 1
                
            stack.pop()

file = open("SCC.txt")

n = 6400

graph = [[] for i in range(0,n+1)]
rev_graph = [[] for i in range(0,n+1)]

explored = [0 for i in range(0,n+1)]
leader = [0 for i in range(0,n+1)]
fin_times = [0 for i in range(0,n+1)]
processed = [0 for i in range(0,n+1)]

for i, line in enumerate(file):   
    u, v = [int(x) for x in line.split()]
    
    graph[u].append(v)
    rev_graph[v].append(u)
    
file.close()

t = 0
s = None

for v in tqdm(range(1,n+1)):
    if not explored[v]:
        s = v
        DFS(rev_graph, v, True)
        
t = 0
s = None

explored = [0 for i in range(0,n+1)]
fin_times = fin_times[::-1][:-1]

for v in tqdm(fin_times):
    if not explored[v]:
        s = v
        DFS(graph, v, False)

SCC = {}
        
for l in leader:
    if l not in SCC:
        SCC[l] = 1
    else:
        SCC[l] += 1
        
groups = sorted(SCC, key=SCC.get)[::-1][:5]

output = [str(SCC[group]) for group in groups]

print(",".join(output))