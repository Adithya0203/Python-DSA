size = int(input("Enter size: ")) # size >= 5 = increasing heart size
alpha = 65
for i in range(int(size/2),size,2):
    # print first spaces
    for j in range(1,size - i,2):
        print(" ",end=" ")
    # print first alphabets
    for j in range(1,i + 1):
        print(chr(alpha + j -1),end = " ")
    # print second spaces
    for j in range(1,size - i + 1):
        print(" ",end = " ")
    # print second alphabets
    for j in range(1,i + 1):
        print(chr(alpha + j -1),end = " ")
    print("")

    # lower part -> inverted pyramid
for i in range(size,0,-1):
    for j in range(0,size - i):
        print(" ",end = " ")
        
    for j in range(1,i * 2):
        print(chr(alpha + j -1),end = " ")
        
    print("")