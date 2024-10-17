for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or (row == col == 3) or (row,col) in ((1,5),(5,1),(2,4),(4,2)): 
             print("Z",end = " ")
        else:
            print(" ",end = " ")
    print("")
    
#----------------------------------------------------------
    
for row in range(7):
    for col in range(7):
        if (row == 0 or row == 6) or row + col == 6: 
             print("Z",end=" ")
        else:
            print(" ",end=" ")
    print("")