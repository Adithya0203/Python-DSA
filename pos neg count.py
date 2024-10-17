pcount = 0
ncount = 0
zero_count = 0
while True:
    num = input("Enter a number: ")
    if num == "":
        break
    num = int(num)
    if num > 0:
        pcount += 1
    elif num < 0:
        ncount += 1
    else:
        zero_count += 1
print(f"Positive numbers: {pcount}")
print(f"Negative numbers: {ncount}")
print(f"Zeroes: {zero_count}")

a=1
b=2
c=3

a,b,c = map(int,input().split())
print(a,b,c)