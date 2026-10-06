#stack operations-push
stack=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    stack.append(value)
print("Stack:",stack)