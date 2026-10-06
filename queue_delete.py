#insert operation in queue and delete operation
from queue import Queue
q=Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
print(list(q.queue))
removed=q.get()
print(list(q.queue))