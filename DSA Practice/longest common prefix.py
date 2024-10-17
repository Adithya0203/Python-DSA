def longestCommonPrefix(strs):
    op = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return op
        op += strs[0][i]
    return op

strs = [i for i in input("Enter space seperated strings: ").split()]
print(longestCommonPrefix(strs))

#--------------------------------------------------

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

strs = [i for i in input("Enter space seperated strings: ").split()]
print(longestCommonPrefix(strs))