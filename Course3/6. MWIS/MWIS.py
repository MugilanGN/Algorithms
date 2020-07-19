weights = [0]
v = 1000

file = open("MWIS.txt")

for i,line in enumerate(file):
    weights.append(int(line))
    
file.close()

A = [0 for i in range(0,v+1)]
A[0] = 0
A[1] = weights[1]

for i in range(2,v+1):
    if A[i-1] > (A[i-2] + weights[i]):
        A[i] = A[i-1]
    else:
        A[i] = A[i-2] + weights[i]

nodes = []
i = v

while i >= 1:
    if A[i-2] + weights[i] > A[i-1]:
        nodes.append(i)
        i -= 1
    i -= 1
    
vertices = [1,2,3,4,17,117,517,997]
bit_string = ""

for vertex in vertices:
    if vertex in nodes:
        bit_string += "1"
    else:
        bit_string += "0"
        
print(bit_string)