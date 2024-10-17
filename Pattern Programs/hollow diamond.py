def run():
    j = 5 # initial stars in upper triangle
    k = 5 # number of columns for the diamond   
    p = 1 # initial row number for lower triangle
    for i in range(4):
        print (" " *k," *" *i)
        k -=1
    while j > 1:
        j -= 1
        print (" "*p," *"*j)
        p +=1
run()