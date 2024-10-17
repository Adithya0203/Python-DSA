def freqCount(arr,n):
    visited = [False] * n
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        print("Element\tCount")
        print(arr[i],'\t',count)
        
arr = list(map(int,input("Enter space seperated values: ").strip().split()))
n = len(arr)
freqCount(arr, n)
#----------------------------------------
print("\n")
#----------------------------------------

def freqcount(arr,n):
    map = {}
    for i in range(n):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    for ele in map:
        print(ele,"\t",map[ele])
        
arr = list(map(int,input("Enter space seperated values: ").strip().split()))
n = len(arr)
freqcount(arr, n)