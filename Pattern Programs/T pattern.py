for row in range(7):
    for col in range(7):
        if row == 0 or col == 3: 
             print("T",end=" ")
        else:
            print(" ",end =" ")
    print("")