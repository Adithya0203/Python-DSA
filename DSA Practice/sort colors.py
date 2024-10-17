def sortColors(nums):
    l,m = 0,0
    h = len(nums) - 1
    while m <= h:
        if nums[m] == 0:
            nums[l],nums[m] = nums[m],nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[m],nums[h] = nums[h],nums[m]
            h -= 1
    return nums

nums = [int(i) for i in input("Enter space seperated elements: ").split()]
print(sortColors(nums))