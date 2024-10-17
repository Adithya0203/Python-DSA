for row in range(7):
    for col in range(7):
        if row == 0 or row == 3 or col == 0:
            print("F",end=" ")
        else:
            print(" ",end=" ")
    print("")