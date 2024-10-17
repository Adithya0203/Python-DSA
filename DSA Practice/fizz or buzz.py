for A in range (1,101):
    if A%3==0 and A%5==0:
        print("FIZZBUZZ",end= " ")
    elif A%3==0:
        print ("FIZZ",end= " ")
    elif A%5==0:
        print ("BUZZ",end= " ")
    else:
        print (A,end= " ")

#------------------------------------------------

def fizzBuzz():
    ip = int(input("Enter the last number: "))
    op = []
    num = 1
    while(num <= ip):
        if (num % 3 == 0 and num % 5 == 0):
            op.append("FizzBuzz")
        elif (num % 3 == 0):
            op.append("Fizz")
        elif (num % 5 == 0):
            op.append("Buzz")
        else:
            op.append(num)
        num += 1
    print(*op)

fizzBuzz()