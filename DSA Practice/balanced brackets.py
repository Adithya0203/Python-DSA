def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack[-1]:
                return False
            stack.pop()
    return not stack

expr = input()
print(is_balanced(expr))