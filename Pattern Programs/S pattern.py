for row in range(7):
    for col in range(7):
        if (((row == 0 or row == 3 or row == 6) and col > 1 and col < 5) or (col == 1 and (row == 1 or row == 2 or row == 6)) or (col == 5 and (row == 0 or row == 4 or row == 5))):
             print("S", end =" ")
        else:
            print(" ", end =" ")
    print("")