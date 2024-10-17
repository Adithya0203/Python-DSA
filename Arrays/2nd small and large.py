def s_smallest(arr):
    n = len(arr)
    if (n < 2):
        return -1
    small = float('inf')
    ssmall = float('inf')
    for i in range(n):
        if arr[i] < small:
            ssmall = small
            small = arr[i]
        elif (arr[i] < ssmall and arr[i]!= small):
            ssmall = arr[i]
    print (ssmall)

def s_largest(arr):
    n = len(arr)
    if (n < 2):
        return -1
    large = float('-inf')
    slarge = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            slarge = large
            large = arr[i]
        elif (arr[i] > slarge and arr[i]!= large):
            slarge = arr[i]
    print (slarge)
    
arr = list(map(int,input("Enter space seperated array elements:\n").split()))
s_smallest(arr)
s_largest(arr)