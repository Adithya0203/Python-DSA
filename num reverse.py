for t in range(int(input())):
    num = int(input())
    rev = 0
    while(num):
        rem = num % 10
        rev = rev * 10 + rem
        num = num//10
    print(rev)