#stack operations-pop
stack=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    stack.append(value)
print("Stack:",stack)
print("pop element/removed element:",stack.pop())