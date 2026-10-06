#Merge two Stacks
stack1=[]
stack2=[]
merged=[]
n1=int(input("Enter number of elements:"))
for i in range(n1):
    value=int(input("Ente value:"))
    stack1.append(value)
n2=int(input("Enter number of elements:"))
for i in range(n2):
    value=int(input("Enter value:"))
    stack2.append(value)
i,j=0,0
while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        merged.append(stack1[i])
        i+=1
    else:
        merged.append(stack2[j])
        j+=1
while i<len(stack1):
    merged.append(stack1[i])
    i+=1
while j<len(stack2):
    merged.append(stack2[j])
    j+=1
print(merged)