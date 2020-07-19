from math import sqrt, floor
from tqdm import tqdm

def euc_dist(a,b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    return dist

file = open("TSPH.txt")

cities = []

for i, line in enumerate(file):
    if i == 0:
        n = int(line)
        continue
    
    c, x, y = [float(x) for x in line.split()]
    
    cities.append([x,y])
    
file.close()

unvisited_cities = [i for i in range(1,n)]
total_dist = 0
j = 0

for visited in tqdm(range(1,n)):
    
    min_dist = float('inf')
    candidates = []

    for s in range(0, n - visited):
            
        i = unvisited_cities[s]    
            
        dist = euc_dist(i,j)

        if min_dist > dist:
            candidates = [i]
            min_dist = dist

        elif min_dist == dist:
            candidates.append(i)

    j = min(candidates)
    
    unvisited_cities.remove(j)

    total_dist += min_dist
    
total_dist += euc_dist(0,j)

print(floor(total_dist))