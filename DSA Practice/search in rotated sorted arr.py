def binarySearch(arr, target,start,end):
    while start <= end:
        mid = start + ((end-start)//2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def peak(arr):
    start,end = 0,len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] > start:
            end = mid - 1
        else:
            start = mid + 1
    return len(arr) - 1 

def search(arr,target):
    peakIndex = peak(arr)
    if target < arr[0]:
        return binarySearch(arr,target,peakIndex + 1,len(arr)-1)
    else:
        return binarySearch(arr,target,0,peakIndex)

arr = [int(i) for i in input("Enter space seperated elements: ").split()]    
element = int(input("Enter element to search: "))
print(search(arr,element))

#----------------------------------------------------------------

def search(nums,target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                    right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

arr = [int(i) for i in input("Enter space seperated elements: ").split()]    
element = int(input("Enter element to search: "))
print(search(arr,element))
#----------------------------------------------------------------