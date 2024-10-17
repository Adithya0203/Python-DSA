for row in range(8):
    for col in range(7):
        if ((col == 0 or col == 6) and row < 5) or ((row - col == 4) and row > 4) or (row == 6 and col == 4) or (row == col == 5): 
             print("U",end=" ")
        else:
            print(" ",end =" ")
    print("")