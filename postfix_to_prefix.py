#prefix to postfix
expression=input("Enter expression:")
stack=[]
for ch in expression[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        b=stack.pop()
        a=stack.pop()
        stack.append(ch+a+b)
print(stack[-1])