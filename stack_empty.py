#stack operations-Empty
stack=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    stack.append(value)
print("Stack:",stack)
while len(stack)>0:
    print("Popped:",stack.pop())
if len(stack)==0:
    print("Stack Empty")