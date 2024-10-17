for row in range(4):
    for col in range(7):
        if ((row == col) and col < 4) or ((row + col == 6) and col > 3):
             print("V",end=" ")
        else:
            print(" ",end =" ")
    print("") 