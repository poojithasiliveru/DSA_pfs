#Monotonic stack decresing order
arr=list(map(int,input("Enter elements:").split()))
stack=[]
for val in arr:
    while stack and stack[-1]<val:
        stack.pop()
    stack.append(val)
print(*stack)