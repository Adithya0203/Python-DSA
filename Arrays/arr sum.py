n = int(input("Enter length of array: "))
a = []
sum = 0
print("Enter the elements")
for i in range(n):
    a.append(int(input()))
    sum += a[i]
print("The sum is",sum)