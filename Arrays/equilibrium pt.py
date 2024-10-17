arr = [int(i) for i in input().split()]
n = len(arr)
if n == 1:
    print(1)
elif n == 2:
    print(-1)
else:
    sumArr = []
    sum = 0
    for i in arr:
        sum += i
        sumArr.append(sum)
    total = sumArr[-1]
    for i in range(1,n-1):
        lsum = sumArr[i] - arr[i]
        rsum = total - sumArr[i]
        if lsum == rsum:
            print(i+1)