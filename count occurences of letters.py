s = input()
arr = []
for i in range(len(s)):
    ch = s[i]
    arr[ch - "a"] += 1

for i in range(len(s)):
    c = s[i]
    if arr[c - "a"] > 0:
        print(c + "" + arr[c - "a"])
    arr[c - "a"]