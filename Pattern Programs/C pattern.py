for row in range(8):
    for col in range(8):
        if (((row == 0 or row == 7) and col > 0) or (col == 0 and (row != 0 and row != 7))):
            print("C", end="")
        else:
            print(" ", end="")
    print()