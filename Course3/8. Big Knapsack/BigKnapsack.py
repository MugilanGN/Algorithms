import sys

def compute(weight,index):
    
    if weight == 0 or index == -1:
        return 0
    
    item = items[index]
    
    if item[1] > weight:
        if item not in cache:
            if (weight,index - 1) not in cache:
                cache[(weight,index-1)] = compute(weight,index-1)
        return cache[(weight,index-1)]
    else:
        if (weight - item[1], index - 1) not in cache:
            cache[(weight - item[1], index - 1)] = compute(weight - item[1], index - 1)
            
        with_item = item[0] + cache[(weight - item[1], index - 1)]
        
        if (weight, index - 1) not in cache:
            cache[(weight,index - 1)] = compute(weight, index - 1)
    
        without_item = cache[(weight,index - 1)]
        
    return max(with_item,without_item)

sys.setrecursionlimit(3000)

weight = 2000000  
item_count = 2000

file = open("BigKnapsack.txt")

items = []

for i,line in enumerate(file):
    v, w = [int(x) for x in line.split()]
    items.append((v,w))
    
file.close()

cache = {}

print(compute(weight,item_count-1))
