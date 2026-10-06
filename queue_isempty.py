#check whether Queue is empty or not
from queue import Queue
q=Queue()
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    q.put(value)
print(list(q.queue))
while not q.empty():
    removed=q.get()
    print(removed,"deleted")
if q.empty():
    print("Queue is empty")
else:
    print(list(q.queue))