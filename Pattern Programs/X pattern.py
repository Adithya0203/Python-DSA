for row in range(7):
    for col in range(7):
        if (row == col) or (row + col == 6):
            print("X",end =" ")
        else:
            print(" ",end =" ")
    print("")