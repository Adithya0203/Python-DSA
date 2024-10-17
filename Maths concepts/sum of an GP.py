a = int(input("enter first term: "))
n = int(input("enter number of terms: "))
r = int(input("enter common ratio: "))

Sn = a * ((r**n) - 1) // (r-1)

print("the sum upto",n,"terms is",Sn)