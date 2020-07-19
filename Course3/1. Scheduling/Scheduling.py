#69119377652,67311454237 = answers

file = open("Scheduling.txt")

jobs = []
diff = []

for i,line in enumerate(file):
    weight,length = [int(x) for x in line.split()]
    jobs.append([weight,length])
    diff.append([weight/length,i])

file.close()

sorted_diffs = sorted(diff, key=lambda x: x[0])[::-1]

total = 0
total_time = 0

while len(sorted_diffs) > 0: 
    val = sorted_diffs[0][0]
    same_stat = []
    
    i = 0
    while i != len(sorted_diffs) and sorted_diffs[i][0] == val:
        same_stat.append(i)
        i+=1
    
    max_index = -1
    max_weight = -100000
    max_index2 = -1
    for i in same_stat:
        index = sorted_diffs[i][1]
        if jobs[index][0] > max_weight:
            max_weight = jobs[index][0]
            max_index = index
            max_index2 = i
    
    total_time += jobs[max_index][1]
    total += total_time * max_weight
    
    del sorted_diffs[max_index2]

print(total)
