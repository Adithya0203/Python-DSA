for row in range(7):
    for col in range(7):
        if col==0 or col==6 or (row==4 and col==2) or (row==5 and col==1) or ((row==col) and (col>2 and col<6)): 
             print("W",end=" ")
        else:
            print(" ",end =" ")
    print("") 