#infix to postfix expression
def precedence(op):
    if op=='+' or op=='-':
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^':
        return 3
    return 0
expression=input("Enter a infix expression:")
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
postfix=''.join(output)
print(postfix)