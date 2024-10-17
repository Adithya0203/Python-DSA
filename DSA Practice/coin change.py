num = int(input("Enter amount: "))
one,two = 0,0
five = (num - 4) // 5
if (((num - 5 * five) % 2) == 0):
    one = 2
else:
    one = 1

two = (num - 5 * five - one) // 2

print("Total coins:",one + two + five)
print("Fives:",five)
print("Twos:",two)
print("Ones:",one)