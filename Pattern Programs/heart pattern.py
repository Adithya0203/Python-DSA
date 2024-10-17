size = int(input("Enter size (min 5): ")) # size >= 5 = increasing heart size
alpha = 65
for i in range(int(size/2),size,2):
    # print first spaces
    for j in range(1,size - i,2):
        print(" ",end=" ")
    # print first H's
    for j in range(1,i + 1):
        print("♥",end = " ")
    # print second spaces
    for j in range(1,size - i + 1):
        print(" ",end = " ")
    # print second H's
    for j in range(1,i + 1):
        print("♥",end = " ")
    print("")

    # lower part -> inverted pyramid
for i in range(size,0,-1):
    for j in range(0,size - i):
        print(" ",end = " ")
        
    for j in range(1,i * 2):
        print("♥",end = " ")
        
    print("")