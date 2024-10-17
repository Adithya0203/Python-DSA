for row in range(6):
    for col in range(6):
        if col == 0 or row == 5:
             print("L",end=" ")
        else:
            print(" ",end=" ")
    print("")