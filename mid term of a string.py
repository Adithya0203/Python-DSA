# program that takes a string and retuns it middle term(s)

ip = input()
size = len(ip)
if len(ip) & 1:
    print(ip[size // 2])
else:
    print(ip[size // 2 - 1],ip[(size // 2)])