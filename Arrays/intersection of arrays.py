def intersection(nums1,nums2):
    visited = set(nums1)
    op = []
    for n in nums2:
        if n in visited:
            op.append(n)
            visited.remove(n)
    return op

nums1 = [int(i) for i in input("Enter space seperated list values: ").split()]
nums2 = [int(i) for i in input("Enter space seperated list values: ").split()]
print(intersection(nums1,nums2))