from bisect import bisect_left, bisect_right

def twoSum(inter,table):
    t = set()
    
    nums = sorted(table)
    
    for x in nums:
        low = bisect_left(nums,inter[0]-x)
        high = bisect_right(nums,inter[1]-x)
        
        for y in nums[low:high]:
            if y != x:
                t.add(x+y)
    
    return len(t)

def main():
    file = open("2Sum.txt")

    table = set()

    for i,line in enumerate(file):
        num = int(line)
        table.add(num)

    file.close()
    
    interval = [-10000,10000]
    
    print(twoSum(interval,table))

if __name__ == "__main__":
    main()