from itertools import combinations as comb
from math import sqrt, floor
from sys import exit
from tqdm import tqdm

import matplotlib.pyplot as plt

def cost(i,j):
    i = points[i]
    j = points[j]
    x, y = i
    a, b = j
    return sqrt((x-a)**2 + (y-b)**2)

file = open('TSP.txt')

points = []

for i,line in enumerate(file):
    if i == 0:
        n = int(line)
        continue
    
    x, y = [float(x) for x in line.split()]
    
    points.append((x,y))

pointsArr = [i for i in range(1,n)]

A = {}

for m in tqdm(range(1,n+1)):
    for S in list( comb( [0] + pointsArr, m ) ):
        if S == (0,):
             A[(S,0)] = [0,[]]
        else:
            A[(S,0)] = [float('inf'),[]]

idx = 0

for m in tqdm(range(2,n+1)):
    for S in set( comb( pointsArr, m - 1 ) ):
        S = (0,) + S

        for j in S[1:]:
            K = []
            
            s = tuple(x for x in S if x != j)
            
            minx = 100000
            
            for k in s:
                if (A[(s,k)][0] + cost(k,j)) < minx:
                    minx = (A[(s,k)][0] + cost(k,j))
                    idx = k
                
            A[(S,j)] = [0,[]]
            A[(S,j)][0] = minx
            A[(S,j)][1] += A[(s,idx)][1] + [idx]
    
minx = 1000000
idx = 0
S = list(comb( [0] + pointsArr, n ))[0]

for j in range(1,n):
    val = (A[(S,j)][0] + cost(j,0))
    if val < minx:
        minx = val
        idx = j
    
print(floor(minx),A[(S,idx)][1])

x = []
y = []

for i in range(0,n-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    
    plt.plot([x1,x2],[y1,y2], 'ro-')
    
    xavg = (x1 + x2)/2
    yavg = (y1 + y2)/2
    
    if x1-x2 == 0:
        pass
    else:
        grad = (y1 - y2)/(x1 - x2)
    
        plt.arrow(xavg, yavg, 1, grad, shape='full', lw=0, length_includes_head=True, head_width=100)
    
plt.plot(points[idx][0],points[idx][1],'bo')
plt.plot(points[0][0],points[0][1],'go')

plt.show()