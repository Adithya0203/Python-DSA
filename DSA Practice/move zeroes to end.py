nums = list(map(int,input("Enter space seperated elements: ").split()))
size = len(nums)
i,j = 0,1
while j < size:
    if nums[i] == 0:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j += 1
        else:
            j += 1
    else:
        i += 1
        j += 1
print(nums)