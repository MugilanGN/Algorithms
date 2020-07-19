weight = 10000 
item_count = 100

#2493893

file = open("Knapsack.txt")

items = []

for i,line in enumerate(file):
    v, w = [int(x) for x in line.split()]
    items.append([v,w])
    
file.close()

a = [[0 for i in range(0,weight+1)] for i in range(0,2)]

for i in range(1,item_count+1):
    
    x = i % 2
    xn = (i - 1) % 2
    v,w = items[i-1]
    
    for j in range(0,weight+1): 
        
        if j >= w:
            a[x][j] = max([a[xn][j],a[xn][j-w]+v])
        else:
            a[x][j] = a[xn][j]

print(max(a[0][weight],a[1][weight]))