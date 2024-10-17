a = int(input("enter first term: "))
n = int(input("enter term number: "))
r = int(input("enter common ratio: "))

An = a * (r ** (n-1))

print("the",n,"th term of the GP is ",An)