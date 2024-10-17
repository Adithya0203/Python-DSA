# max = 100

n = int(input("Enter n (min 3): ")) # n >= 3 to view pattern
size = n
first = 0
last = size - 1
arr = [[0 for i in range(n)] for i in range(n)]

while n != 0:
    for i in range(first,last+1):
        for j in range(first,last+1):
            if i == first or i == last or j == first or j == last:
                arr[i][j] = n
        
    first += 1
    last -= 1
    n -= 1
    
for i in range(size):
    for j in range(size):
        print(arr[i][j],end=" ")
    print(" ")

#------------------------------------------------------------------

n = int(input("Enter n (min 2): ")) # n >= 3 to view pattern
size = 2 * n
for i in range(1,size):
    for j in range(1,size):
        print(max(abs(n-i),abs(n-j)) + 1,end=" ")
    print("")