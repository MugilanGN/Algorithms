def find(u):
    org = u
    while u != sets[u]:
        u = sets[u]
    while org != sets[org]:
        thing = sets[org]
        sets[org] = u
        org = thing
    return u

def dist(u,v):
    d = 0
    for i,bit in enumerate(u):
        if bit != v[i]:
            d += 1
    return d

file = open("BigClusters.txt")

nodes = []
nums = {}

sets = [i for i in range(0,200000)]

for i,line in enumerate(file):
    num = str("".join(line.split()))
    nodes.append([i,num])
    nums[int(num,2)] = [i,num]

file.close()

distances = [(2**i+2**j) for i in range(0,23) for j in range(i+1,24)]
distances.extend([(2**i-2**j) for i in range(0,23) for j in range(i+1,24)])
distances.extend([2**i for i in range(0,24)])
distances.extend([-i for i in distances])
distances.extend([0])

count = 0
track = 0
for distance in distances:
    for nodem in nodes:
        ind = nodem[0]
        node = int(nodem[1],2)
        if (node+distance) in nums:
            if find(nums[node+distance][0]) != find(ind):
                hamming = dist(nums[node+distance][1],nodem[1])
                if hamming < 3:
                    count += 1
                    sets[find(nums[node+distance][0])] = find(ind)
    
    track += 1
                
                
print(len(nodes) - count)
            
            