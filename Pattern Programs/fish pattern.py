def drawPattern(n):
    sp1 = ""
    st1 = "*"
    st2 = ""
    
    for i in range(n):
        sp1 += ' '
        
    for j in range(2 * n + 1):
        if (j < n):
            print(sp1 + st1 + sp1 + sp1,end =" ")
            print(st2)
            sp1 = sp1[0:len(sp1) - 1]
            st1 += "**"
            st2 += "*"
            
        if (j == n):
            print(sp1 + st1 + sp1 + sp1,end = " ")
            print(st2)
            
        if (j > n):
            sp1 += ' '
            st1 = st1[0:len(st1)-1]
            st1 = st1[0:len(st1)-1]
            st2 = st2[0:len(st2)-1]
            print(sp1 + st1 + sp1 + sp1,end = " ")
            print(st2)
            
n = int(input("Enter value of N (min 2): ")) # n>= 2 for correct design
print(drawPattern(n))