def swap(arr, a, b, k): # a,b are indexes
    for i in range(k):
        temp = arr[a + i]
        arr[a + i] = arr[b + i] # items at index a+i and b+i is swapped
        arr[b + i] = temp

def BlockSwap(arr, k, n):
    if k == 0 or k == n: # no blocks or is in single block
        return
    if k == n - k: # same size blocks
        swap(arr, 0, n - k, k) # items at index 0 and n-k is swapped
        return
    elif k < n - k: # first part is smaller
        swap(arr, 0, n - k, k) # items at index 0 and n-k is swapped
        BlockSwap(arr, k, n - k) # roatate second part
    else: # second part is smaller
        swap(arr, 0, k, n - k) # items at index 0 and n-k is swapped
        BlockSwap(arr[n - k:], 2 * k - n, k) # function called in remaining part of array

arr = list(input("Enter the space seperated list: ").split())
n = int(input("Enter n: "))
k = int(input("Enter k: "))
BlockSwap(arr, k, n)
print("After rotating the array:")
for i in range(n):
    print(arr[i], end=" ")