#balance the unbalanced paranthesis
expression=input("Enter the expression:")
stack=[]
result=''
for ch in expression:
    if ch=='(':
        stack.append(ch)
        result+=ch
    elif ch==')':
        if len(stack)>0:
            stack.pop()
            result+=ch
        else:
            result="("+result+ch
    else:
        result+=ch
while len(stack)>0:
    result+=')'
    stack.pop()
print("Balanced expression:", result)