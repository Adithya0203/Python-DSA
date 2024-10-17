def remove_duplicates(arr):
    unique = []
    for element in arr:
        if element not in unique:
            unique.append(element)
    unique.sort()
    return unique

arr = [int(i) for i in input("Enter space seperated list values: ").split()]
# [4, 3, 9, 2, 4, 1, 10, 89, 34]
print(remove_duplicates(arr))