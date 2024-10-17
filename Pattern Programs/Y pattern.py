for row in range(7):
    for col in range(7):
        if (((col == 1 or col == 5) and row < 2) or (row == col and col > 0 and col < 4) or (col == 4 and row == 2) or ((col == 3) and row > 3)):
            print("Y"),
        else:
            print(" "),
    print("")