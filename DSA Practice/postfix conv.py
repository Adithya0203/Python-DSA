class Conversion:# Constructor to initialize the class variables 
    def __init__(self, capacity):
        self.top = -1 
        self.capacity = capacity 
        self.array = [] 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
 
    def isEmpty(self):
        if self.top == -1:
            return True
        else :
            return False
  
    def peek(self):
        return self.array[-1] 
  
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op) 
 
    def isOperand(self, ch):
        return ch.isalpha()
 
    def notGreater(self, i): # Check if the precedence of operator < stack top
        try:
            a = self.precedence[i]
            c=self.peek()
            b = self.precedence[c]
            #print(i,c,a<=b)
            if a <= b :
                return True
            else :
                return False
        except KeyError:
                return False

 # Function to convert infix expression to postfix expression
    def infixToPostfix(self, exp):
        for i in exp: 
            if self.isOperand(i):
                self.output.append(i)  
            elif i == '(':
                self.push(i)  
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    print("Popped ",a)
                    self.output.append(a) 
                    if (self.peek() == '('):
                        self.pop()
                        break
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    c=self.pop()
                    #print("Popped ",c)
                    self.output.append(c)
                self.push(i)
 
        print("\nPostfix Notation : ")
        while not self.isEmpty():
            self.output.append(self.pop()) 
            print("".join(self.output)) 

# Driver code
# "A+(B*C-(D/E-F)*G)*H"
exp=input("Enter the expression: ")
print("\n\nInfix Notation :",exp)
obj = Conversion(len(exp)) 
obj.infixToPostfix(exp)