arr = list(map(int,input("Enter space seperated values: ").strip().split()))
arr.sort()
print(arr)
n = len(arr)
if n % 2 == 0:
    ind1 = (n // 2) - 1
    ind2 = n // 2
    median = (arr[ind1] + arr[ind2]) // 2
else:
    median = (arr[n//2])
print(median)