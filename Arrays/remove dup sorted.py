arr = [int(i) for i in input("Enter space seperated list values: ").split()]
st = set()
for i in range(len(arr)):
    st.add(arr[i])
n = len(st)
j = 0
for ele in st:
    arr[j] = ele
    print(ele,end=" ")
    j += 1
#----------------------------------------------------------------------
from typing import List
def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

if __name__ == "__main__":
    arr = list(map(int,input("Enter space seperated values: ").split()))
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")