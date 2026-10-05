#Remove unbalanced paranthesis
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
        result+=ch
while len(stack)>0:
    temp=''
    count=0
    for ch in result:
        
        if ch=='(' and count<len(stack):
            count+=1
        else:
            temp+=ch
    result=temp
print(result)