
nums = list(map(int,input().split()))
xors = nums[0]
for i in range(1,len(nums)):
    xors ^= nums[i]
print(xors)