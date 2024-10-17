def sqrt(x):
    beg = 1
    end = x

    while(beg <= end):
        mid = (beg + end) // 2
        if mid * mid == x:
            return mid
        elif mid <= x // mid:
            beg = mid + 1
            op = mid
        else:
            end = mid - 1
    return op

x = int(input("Enter the number: "))
print(sqrt(x))