arr = list(map(int,input("Enter space seperated list values: ").split()))   #[10, 9, 14, 8, 20, 48, 16, 9]
print("Enter Position to insert:\n1)Beginning\n2)Ending\n3)Index")
option = int(input())

if option == 1:
    value = int(input("Enter the value: "))
    print("Before inserting the value at the beginning:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    arr.insert(0,value)
    print("After inserting the value at the beginning:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if option == 2:
    value = int(input("Enter the value: "))
    print("Before inserting the value at the beginning:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    arr.append(value)
    print("After inserting the value at the ending:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if option == 3:
    value = int(input("Enter the value: "))
    ind = int(input("Enter Index: "))
    arr.insert(ind-1,value)
    print("Before inserting the value at the beginning:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    print("After inserting the value at the beginning:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()