def prime(n,j):
    if(n<2):
        return "Not prime"
    if(j==n):
        return "prime"
    if(n%j==0):
        return "Not prime"
    return prime(n,j+1)

n=int(input("Enter a number: "))
print(prime(n,2))