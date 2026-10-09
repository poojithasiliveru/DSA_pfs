#Circular queue-insert
from queue import Queue
q=Queue()
arr=list(map(int,input("Enter number of elements:").split()))
for i in arr:
    q.put(i)
value=int(input("Enter value to insert:"))
q.put(value)
n=q.qsize()
print("Circular queue:",end=' ')
for i in range(n+1):
    i=q.get()
    print(i,end=' ')
    q.put(i)