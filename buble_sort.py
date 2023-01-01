def bubble_sort(L):
    n = len(L)

    for i in range(0,n):
        for j in range(0,n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1],L[j]



L = [5,9,1,2,7]
print("Before sorting : ", end="")
print(L)
print("After sorting  : ", end="")
bubble_sort(L)
print(L)