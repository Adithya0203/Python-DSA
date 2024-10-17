from collections import Counter,defaultdict
def frequencySort(s):
    count = Counter(s)
    buckets = defaultdict(list)

    for char,cnt in count.items():
        buckets[cnt].append(char)

    res = []
    for i in range(len(s),0,-1):
        for c in buckets[i]:
            res.append(c * i)
        
    return "".join(res)

s = input("Enter the string: ")
print(frequencySort(s))

#----------------------------------------------

from collections import Counter
import heapq
def frequencySort(s):
    freq_map = Counter(s)
    max_heap = [(-freq, char) for char, freq in freq_map.items()]
    heapq.heapify(max_heap)
    res = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        res.append(char * (-freq))
        return ''.join(res)
    
s = input("Enter the string: ")
print(frequencySort(s))