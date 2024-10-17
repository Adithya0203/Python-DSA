arr = list(map(int,input().strip().split()))
n = len(arr)
sum = 0
for i in range(n):
    sum += arr[i]
avg = sum / n
print(avg)