for r in range (1,8):
    for c in range (1,8):
        if r>1 and r<7 and c>1 and c<7:
            print(" ",end=" ")
        else:
            print("#",end=" ")
    print("")