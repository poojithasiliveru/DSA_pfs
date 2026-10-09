#Circular Delete
queue=list(map(int,input("Enter elements:").split()))
value=int(input("Enter value:"))
n=len(queue)
found=False
for i in range(n):
    index=i%n
    if queue[index]==value:
        found=True
        for j in range(index,n-1):
            queue[j]=queue[j+1]
        queue.pop()
        break
if found:
    print("After Deletion:",queue)
else:
    print("Value not found")
