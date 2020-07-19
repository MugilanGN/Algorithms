from sys import exit
from tqdm import tqdm

def path(i,j,k,l):
    x = A[i][j][l]
    y = A[i][k][l] + A[k][j][l]
    return min(x,y)

file = open("APSP.txt")

for i,line in enumerate(file):
    if i == 0:
        n = [int(x) for x in line.split()][0]
        graph = [[] for i in range(0,n+1)]
        continue
    
    u, v, weight = [int(x) for x in line.split()]
    
    graph[u].append([v,weight])

A = [[[0 for k in range(0,2)] for j in range(0,n)] for i in range(0,n)]

for i in range(0,n):
    for j in range(0,n):
        if i == j:
            A[i][j][0] = 0
            
        L = graph[i]
        M = [x for x, v in enumerate(L) if v[0] == j]
        
        if len(M):
            A[i][j][0] = graph[i][M[0]][1]
        else:
            A[i][j][0] = float('inf')
            
for k in tqdm(range(1,n)):
    x = k % 2
    xn = x - 1
    for i in range(1,n):
        for j in range(1,n):
            A[i][j][x] = path(i,j,k,xn)

for i in range(0,n):
    if A[i][i][1] < 0:
        print("NULL")
        exit()

minx = float('inf')
        
for i in range(0,n):
    for j in range(0,n):
        if A[i][j][1] < minx:
            minx = A[i][j][1]

print(minx)