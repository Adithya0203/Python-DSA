z="H"
for row in range (7): # standing first
    for col in range (5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
            print("H",end=" ") 
        else:
            print(" ",end=" ")
    print("")