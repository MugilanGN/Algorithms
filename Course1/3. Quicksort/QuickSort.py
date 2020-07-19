def QuickSort(A,l,r):
    comparisons = 0
    if l < r:
        comparisons = r - l - 1
        
        p1 = A[l]
        p2 = A[r-1]
        p3 = A[l + (r-l)//2 + ((r-l) % 2 > 0) - 1]
        
        if ((p1 < p2 and p2 < p3) or (p3 < p2 and p2 < p1)) : 
            A[l], A[r-1] = A[r-1], A[l]
        elif ((p2 < p1 and p1 < p3) or (p3 < p1 and p1 < p2)) : 
            pass
        else:
            A[l], A[l + (r-l)//2 + ((r-l) % 2 > 0) - 1] = A[l + (r-l)//2 + ((r-l) % 2 > 0) - 1], A[l]
        
        p = A[l]
        i = l+1

        for j in range(l+1,r):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1

        A[l], A[i-1] = A[i-1], A[l]

        [A,c1] = QuickSort(A,l,i-1)
        [A,c2] = QuickSort(A,i,r)
        
        comparisons += c1 + c2
    
    return [A, comparisons]

def main():
    file = open("QuickSort.txt", "r+")
    raw = file.readlines()
    file.close()
    preprocessed = [int(number[:-1]) for number in raw]
    print(QuickSort(preprocessed,0,len(preprocessed))[1])

if __name__ == "__main__":
    main()
