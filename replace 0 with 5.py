def convert(n):
    op = 0
    if n == 0:
        return 5
    factor = 1
    while (n > 0):
        if n % 10 == 0:
            op += (5 * factor)
        else:
            op += (n % 10 * factor)
        n = n // 10
        factor *= 10
    
    return op
n = int(input())
print(convert(n))