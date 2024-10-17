alist=list(map(int,input().split()))
print("original list is: ",alist)
for i in range (1,len(alist)):
    key=alist[i]
    j=i-1
    while j>0 and key<alist[j]:
        alist[j+1]=alist[j]
        j-=1
    else:
        alist[j+1]=key
print("list after sorting:",alist)