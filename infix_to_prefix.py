#infix to prefix expression
def precedence(op):
    if op=='+' or op=='-':
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^':
        return 3
    return 0
expression=input("Enter a infix expression:")
expression=expression[::-1]
stack=[]
output=[]
for ch in expression:
    if ch.isalnum():
        output.append(ch)
    else:
        while stack and precedence(stack[-1])>=precedence(ch):
            output.append(stack.pop())
        stack.append(ch)
while stack:
    output.append(stack.pop())
prefix=''.join(output[::-1])
print(prefix)