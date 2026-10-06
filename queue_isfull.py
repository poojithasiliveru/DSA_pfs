#check whether Queue is full or not
from queue import Queue,Full
size=int(input("Enter the size:"))
q=Queue(maxsize=size)
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    try:
        q.put_nowait(value)
        print(value,"inserted")
    except:
        print("Queue is Full")
        break
print(list(q.queue))
