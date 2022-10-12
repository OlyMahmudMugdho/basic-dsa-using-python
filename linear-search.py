def linear_search(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return i
    return -1
    
L = [2,4,6,8,10]
x = 6
print(linear_search(L,x))
