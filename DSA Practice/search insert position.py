def searchInsert(arr,target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start + 1

arr = [int(i) for i in input("Enter space seperated elements: ").split()]    
element = int(input("Enter element to insert: "))
print(searchInsert(arr,element))

#-----------------------------------------

def searchInsert(arr,target):
    start, end = 0, len(arr) - 1

    if target > arr[end]:
        return end + 1
    if target < arr[start]:
        return start
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start + 1

arr = [int(i) for i in input("Enter space seperated elements: ").split()]    
element = int(input("Enter element to insert: "))
print(searchInsert(arr,element))

#-----------------------------------------