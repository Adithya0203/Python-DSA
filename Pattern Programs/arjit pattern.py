for row in range(7):    
    for col in range(7):     
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col > 1 and col < 5))):    
            print("A", end =" ")
        else:
            print(" ", end =" ")
    print("")
    
print("\n")

for row in range(6):
    for col in range(5):
        if col == 1 or ((row ==0 or row ==2) and (col > 0 and col < 5)) or ((row - col == 1) and (col > 1 and col < 6)) or (row == 1 and col ==4):
             print("R",end =" ")
        else:
            print(" ",end = " ")
    print("")
    
print("\t")

for row in range(7):
    for col in range(5): 
        if col==2 or (row==0 and col!=2) or (row==6 and col<2):
            print("J",end=" ")
        else:
            print(" ",end=" ")
    print("")
    
print("\t")

for row in range(7):
    for col in range(5):
        if col==2 or((row==0 or row==6)and col!=2):
             print("I",end=" ")
        else:
            print(" ",end=" ")
    print("")
    
print("\t")

for row in range(7):
    for col in range(7):
        if row == 0 or col == 3: 
             print("T",end=" ")
        else:
            print(" ",end =" ")
    print("")