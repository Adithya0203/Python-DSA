for i in range(1,6):
    for k in range(1,i+1):
        print(" ",end = " ")
    for j in range(1,i+1):
        print("*",end = " ")
    for k in range(1,(3*(4 - i + 1))+1):
        print(" ",end = " ")
    for j in range(1,2 * i):
        print("*",end = " ")
    for k in range(1,(3*(4 - i + 1))+1):
        print(" ",end = " ")
    for j in range(1,i+1):
        print("*",end = " ")
    print("")

for i in range(1,3):
    for k in range(1,5+i):
        print(" ",end = " ")
    for j in range(1,(2*(9-i+1)+1)):
        print("*",end = " ")
    print("")