x = int(input("enter first number: "))
y = int(input("enter second number: "))
if x > y:
    smaller = y
else: 
    smaller = x
for i in range(1,smaller + 1):
    if (x % i == 0) and (y % i == 0):
        gcd = i
lcm=(x * y) // gcd
print ("the HCF of", x, "and", y, "is", gcd)
print ("the LCM of", x, "and", y, "is", lcm)