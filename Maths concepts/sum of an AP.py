a = int(input("enter first term: "))
n = int(input("enter number of terms: "))
d = int(input("enter difference: "))

Sn=(n//2) * (2 * a + (n-1) * d)

print("the sum upto",n,"terms is",Sn)