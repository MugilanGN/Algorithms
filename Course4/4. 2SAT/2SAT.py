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

file = open("test.txt")

for i, line in enumerate(file):
    if i == 0:
        m = int(line)
        n = 2 * m + 1
        
        graph = [[] for i in range(0,n)]
        rev_graph = [[] for i in range(0,n)]

        explored = [0 for i in range(0,n)]
        leader = [0 for i in range(0,n)]
        fin_times = [0 for i in range(0,n)]
        processed = [0 for i in range(0,n)]
        
        continue
    
    x, y = [int(x) for x in line.split()]
    
    if x > 0:
        if y > 0:
            graph[x].append(y + m)
            graph[y].append(x + m)
            
            rev_graph[x + m].append(y)
            rev_graph[y + m].append(x)
            
        else:
            rev_graph[-y].append(x)
            rev_graph[x + m].append(-y + m)
            
            graph[x].append(-y)
            graph[-y + m].append(x + m)
    else:
        if y > 0:
            rev_graph[y + m].append(-x + m)
            rev_graph[-x].append(y)
            
            graph[-x + m].append(y + m)
            graph[y].append(-x)

        else:
            rev_graph[-x].append(-y + m)
            rev_graph[-y].append(-x + m)
            
            graph[-y + m].append(-x)
            graph[-x + m].append(-y)
    
file.close()

t = 0
s = None

for v in tqdm(range(1,n)):
    if not explored[v]:
        s = v
        DFS(rev_graph, v, True)
        
t = 0
s = None

explored = [0 for i in range(0,n)]
fin_times = fin_times[::-1][:-1]

for v in tqdm(fin_times):
    if not explored[v]:
        s = v
        DFS(graph, v, False)

correct = 1        

for i in range(1,m+1):
    if leader[i] == leader[i+m]:
        correct = 0
        break

print(correct)
