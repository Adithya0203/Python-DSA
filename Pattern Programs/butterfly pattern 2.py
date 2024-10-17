for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    for k in range(1,(2*(5-i))):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

print("* " * 9)

for i in range(1,5):
    for j in range(1,(3-i+1)+1):
        print("*",end=" ")
    for k in range(1,(2*i)+2):
        print(" ",end=" ")
    for j in range(1,(3-i+1)+1):
        print("*",end=" ")
    print("")