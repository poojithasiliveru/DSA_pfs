#check whether the expression is balance or not
expression=input("Enter the expression:")
stack=[]
for ch in expression:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if len(stack)==0:
            print("Not Balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not Balanced")