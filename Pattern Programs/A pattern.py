for row in range(7):    
    for col in range(7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):    
            print("A", end =" ")
        else:
            print(" ", end =" ")
    print("")