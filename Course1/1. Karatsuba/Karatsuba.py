from math import ceil, floor

def karatsuba(x,y):
    if x < 10 and y < 10:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)  
    
    a = floor(x / 10**m)
    b = x % 10**m
    
    c = floor(y / 10**m)
    d = y % 10**m
    
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd
    
    return int((10**(m*2)) * ac + (10**(m)) * ad_bc + bd)
    
    
def main():
    p2 = karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
    print(p2)

if __name__ == "__main__":
    main()