r = int(input("Enter no of rows: "))
c = int(input("Enter no of columns: "))
mat1 = mat2 = []

print("Enter 1st matrix row wise")
for k in range(r):
    a = []
    for l in range(c):
        a.append(int(input()))
    mat1.append(a)
    
print("Enter 2nd matrix row wise")
for m in range(r):
    b = []
    for n in range(c):
        b.append(int(input()))
    mat2.append(b)

flag = True
row1 = len(mat1)
col1 = len(mat1[0])
row2 = len(mat2)
col2 = len(mat2[0])
if (row1 != row2 or col1 != col2):
    print("Matries are not equal")
else:
    for i in range(row1):
        for j in range(col1):
            if (mat1[i][j] != mat2[i][j]):
                flag = False
                break
    if (flag):
       print("Matrices are equal")
    else:
       print("Matrices are not equal")