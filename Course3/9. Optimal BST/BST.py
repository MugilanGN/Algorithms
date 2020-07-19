def cost(i,j):
    if i > j:
        return 0
    
    elif C[i][j] >= 0:
        return C[i][j]
    
    elif i == j:
        return items[i]
    
    else:
        k = []

        for r in range(i,j+1):
            k.append(cost(i,r-1) + cost(r+1,j))

        return sum(items[i:j+1]) + min(k)

items = [0.05,0.4,0.08,0.04,0.1,0.1,0.23]
n = len(items)

C = [[-100000 for i in range(0,n)] for i in range(0,n)]

for i in range(0,n):
    for j in range(i,n):
        C[i][j] = cost(i,j)

print(C[0][n-1])
        
        