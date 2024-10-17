n=input("enter n: ")
sum_odd=sum_even=0
for a in range(1,n+1,2):
    sum_odd+=a
print("the sum of odd numbers is",sum_odd)
for b in range(2,n+1,2):
    sum_even+=b
print("the sum of even nos is",sum_even)