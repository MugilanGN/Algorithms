from heapq import heappush,nsmallest,heappop

file = open("Median.txt")

h_low = []
h_high = []

Sum = 0

for i,line in enumerate(file):
    cont = True
    if i == 0:
        heappush(h_high,int(line))
        cont = False
    if i == 1:
        heappush(h_low,-int(line))
        cont = False
    
    if cont:
        if int(line) > -h_low[0]:
            if int(line) > h_high[0]:
                heappush(h_high,int(line))
            else:
                if len(h_low) > len(h_high):
                    heappush(h_low,-int(line))
                else:
                    heappush(h_high,int(line))

        else:
            heappush(h_low,-int(line))

        while len(h_low) - len(h_high) > 1:
            val = -heappop(h_low)
            heappush(h_high,val)
        while len(h_high) - len(h_low) > 1:
            val = heappop(h_high)
            heappush(h_low,-val)
    
    k = len(h_low) + len(h_high)
    
    if k % 2 == 1:
        pos = (k+1)/2
        if pos <= len(h_low):
            median = -h_low[0]
            
        else:
            median = h_high[0]
    else:
        pos = k/2
        if pos <= len(h_low):
            median = -h_low[0]
        else:
            median = h_high[0] 
        
    Sum += median
    
    #if i < 20:
        #print(h_low,h_high,median)

        
file.close()

print(Sum % 10000)

