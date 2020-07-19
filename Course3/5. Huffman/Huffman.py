def Huffman(weights):
    q1 = sorted(weights)
    q2 = []
    max_dist = {}
    min_dist = {}
    
    for i in range(0,symbols):
        max_dist[q1[i]] = 0
        min_dist[q1[i]] = 0
    
    for i in range(0,symbols):     
        if len(q1):
            mini = q1.pop(0)
        elif len(q2):
            mini = q2.pop(0)
        else:
            break
        
        if len(q1):
            if len(q2):
                if q1[0] < q2[0]:
                    mini2 = q1.pop(0)
                else:
                    mini2 = q2.pop(0)
            else:
                mini2 = q1.pop(0)
        else:
            if len(q2):
                mini2 = q2.pop(0)
            else:
                break
        
        combined = mini+mini2
        
        max_dist[combined] = max([max_dist[mini],max_dist[mini2]]) + 1
        
        min_dist[combined] = min(min_dist[mini],min_dist[mini2]) + 1
        
        q2.append(combined)
    
    print(max_dist[max(max_dist, key=max_dist.get)])
    
    print(min_dist[max(min_dist, key=min_dist.get)])
    
symbols = 1000

file = open("Huffman.txt")

weights = []

for i,line in enumerate(file):
    weights.append(int(line))
    
file.close()
    
Huffman(weights)