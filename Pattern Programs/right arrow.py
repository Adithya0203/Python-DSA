rows = int(input("Enter no of rows (min 5): "))
for i in range(0,rows-1):
    for j in range(0,i):
        print("*" + " ",end=" ")
    print("")
    
for i in range(rows-1,0,-1):
    for j in range(0,i-1):
        print("*" + " ",end=" ")
    print("")