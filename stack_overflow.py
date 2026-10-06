#Stack operation - overflow condition
stack=[]
size=int(input("Enter size of the stack:"))
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    if len(stack)<size:
        stack.append(value)
        print("Pushed value:",value)
    else:
        print("Stack Overflow...")
print("Stack is:",stack)