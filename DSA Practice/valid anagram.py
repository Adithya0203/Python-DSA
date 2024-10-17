def valid_anagram(s,t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

str1 = input("Enter string 1: ")
str2 = input("Enter String 2: ")
print(valid_anagram(str1,str2))

#----------------------------------------------------------

def valid_anagram(s,t):
    map1,map2={},{}
    for i in s:
        map1[i] = s.count(i)
    for j in t:
        map2[j] = t.count(j)
    if map1 == map2:
        return True
    else:
        return False
  
str1 = input("Enter string 1: ")
str2 = input("Enter String 2: ")
print(valid_anagram(str1,str2))