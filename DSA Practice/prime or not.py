n=int(input("Enter number: "))
lim=int(n/2)+1
for i in range (2,lim):
    rem=n%i
    if rem==0:
        print(n,"is a composite number")
        break
else:
    print(n,"is a prime number")