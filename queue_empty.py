#insert operation in queue check whether it is empty or not
from queue import Queue
q=Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)

if q.empty():
    print("Queue is Empty")
else:
    print(list(q.queue))