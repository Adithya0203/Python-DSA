n = int(input("Number: "))
bin = []
while n > 0:
    if n % 2 == 1:
        bin.append(1)
    else:
        bin.append(0)
    n //= 2
bin.reverse()
for bit in bin:
    print(bit, end="")