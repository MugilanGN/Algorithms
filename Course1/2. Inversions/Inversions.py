def countInversions(A):
    if len(A) <= 1:
        return [A,0]
    
    inv_count = 0
    
    B = A[:len(A)//2]
    C = A[len(A)//2:]

    [sortedB,invs] = countInversions(B)
    [sortedC,invs2] = countInversions(C)
    
    inv_count += invs + invs2
    
    i, j = 0, 0
    
    for k in range(0,len(A)):
        
        if i >= len(sortedB):
            for k in range(k,len(A)):
                A[k] = sortedC[j]
                j += 1
            break
            
        if j >= len(sortedC):
            for k in range(k,len(A)):
                A[k] = sortedB[i]
                i += 1
            break
        
        if sortedB[i] < sortedC[j]:
            A[k] = sortedB[i]
            i += 1
        else:
            A[k] = sortedC[j]
            j += 1
            inv_count += len(sortedB) - i

    return [A,inv_count]

def main():
    file = open("Inversions.txt", "r+")
    raw = file.readlines()
    file.close()
    preprocessed = [int(number[:-1]) for number in raw]
    print(countInversions(preprocessed)[1])
    
if __name__ == "__main__":
    main()


