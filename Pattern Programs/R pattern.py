for row in range(6):
    for col in range(5):
        if col == 1 or ((row ==0 or row ==2) and (col > 0 and col < 5)) or ((row - col == 1) and (col > 1 and col < 6)) or (row == 1 and col ==4):
             print("R",end =" ")
        else:
            print(" ",end = " ")
    print("")