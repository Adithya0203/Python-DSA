arr = [int(i) for i in input("Enter space seperated list values: ").split()]
n = len(arr)
max = arr[n-1]
print(max,end=" ")
for i in range(n-2,-1,-1):
    if arr[i] >= max:
        print(arr[i],end=" ")
        max = arr[i]