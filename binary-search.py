def binary_search(L,x):
    low = 0
    high = len(L)-1
    
    while(low<=high):
        mid = (low+high)//2
        if L[mid]==x:
            return mid
        if L[mid]<x:
            low = mid+1
        else:
            high = mid-1
            
    return -1
    
L = [2,4,6,8,10,12,14]
x  = 10
res = binary_search(L,x)
print(res)