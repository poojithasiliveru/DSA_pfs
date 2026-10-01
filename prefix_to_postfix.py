#prefix to postfix
expression=input("Enter expression:")
stack=[]
for ch in expression[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b+ch)
print(stack[-1])