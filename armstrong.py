low = int(input("Lower range: "))
up = int(input("Upper range: "))
for num in range(low,up+1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp //= 10
    if num == sum:
        print(num)