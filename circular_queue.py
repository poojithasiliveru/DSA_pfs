#circular queue
arr=list(map(int,input("Enter elements:").split()))
start=int(input("Enter starting point:"))
n=len(arr)
print("Traversal:")
for i in range(n):
    index=(start+i)%n
    print(arr[index],end=' ')
