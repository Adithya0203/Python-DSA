arr = arr = list(map(int,input("Enter space seperated values: ").strip().split()))
op = []
n = len(arr)
for ele in range(n-1,-1,-1):
    op.append(arr[ele])
print(op)
# ----------------------------------------------------------
arr = arr = list(map(int,input("Enter space seperated values: ").strip().split()))
n = len(arr)
p1,p2 = 0,n-1
while p1 < p2:
    arr[p1],arr[p2] = arr[p2],arr[p1]
    p1 += 1
    p2 -= 1
print(arr)
# ----------------------------------------------------------
def reverseArr(arr,start,end):
    if start < end:
        arr[start],arr[end] = arr[end],arr[start]
        reverseArr(arr,start+1,end-1)
        
def printArr(arr,n):
    for ele in arr:
        print(ele,end=" ")
    print(" ")
    
arr = arr = list(map(int,input("Enter space seperated values: ").strip().split()))
n = len(arr)
reverseArr(arr,0,n-1)
printArr(arr,n)
# ----------------------------------------------------------