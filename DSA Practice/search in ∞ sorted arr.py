def binary_search(arr,target,start,end):
    while start <= end:
        mid = start + ((end-start)//2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binaryInfiniteArray(arr,target):
    start,end = 0,1
    if target > arr[end]:
        newStart = end + 1
        newEnd = end + (end - start + 1) * 2
        binary_search(arr,target,newStart,newEnd)
    binary_search(arr,target,start,end)

# [[2,6,9,10,17,25,48,51,87,98,100,102,120,130,140]]
arr = [int(i) for i in input().split()]
target = 140
print(binaryInfiniteArray(arr,target))