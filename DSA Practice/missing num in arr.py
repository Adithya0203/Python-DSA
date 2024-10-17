nums = [int(i) for i in input("Enter space seperated elements: ").split()]
n = len(nums)
arrSum = sum(nums)
totalSum = (n+1) * (n+2) // 2
print(totalSum - arrSum)