s=input("enter a string: ")
length,rev=len(str),-1
mid=length/2
for a in range (mid):
    if str[a]==str[rev]:
        a,rev=a+1,rev-1
    else:
        print(str,"is not a palindrome")
        break
else:
    print(str,"is a palindrome")

#-----------------------------------------
i = 0
z = len(s) - 1
while i < z:
    if s[i] != s[z]:
        print("Not a palindrome")
        exit()
    i += 1
    z -= 1
print("Palindrome")