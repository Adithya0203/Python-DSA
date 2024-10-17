n = int(input())
if (n & 1) == 1:
    x = (n // 2) + 1
else:
    x = (n // 2)

print(x**2)