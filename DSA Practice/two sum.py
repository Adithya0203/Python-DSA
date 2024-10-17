def twoSum(nums,target):
    n = len(nums)
    op = []
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] + nums[j]) == target:
                op.append(i)
                op.append(j)
                break
            else:
                continue
    return(op)

print(twoSum([3,2,4],6))

#------------------------------------------------------

def twoSum(nums,target):
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            return (map[nums[i]],i)
        map[target-nums[i]] = i

print(twoSum([3,2,4],6))

#------------------------------------------------------