ch=input("enter a single character: ")
if ch>='A' and ch<='Z':
    print("it is an uppercase character")
elif ch>='a' and ch<='z':
    print("it is a lowercase character")
elif ch>=1 and ch<= 9:
    print("it is a digit")
else:
    print("it is a special character")