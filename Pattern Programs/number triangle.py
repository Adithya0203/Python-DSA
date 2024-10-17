rows = int(input("Enter no of rows (3-10): "))
print("Here is your pattern \n")
    # upper half
for i in range(1,rows+1):
    # print i spaces at beginning
    for j in range(1,i):
        print(" ",end = " ")
    # printing i to rows value at end of each row
    for j in range(i,rows+1):
        print(j,end = " ")
    print(" ")

# printing lower half

for i in range(rows-1,0,-1):
    # printing i spaces
    for j in range(1,i):
        print(" ",end = " ")
    # printing i to row values at end of each row
    for j in range(i,rows+1):
        print(j,end = " ")
    print(" ")