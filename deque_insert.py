#insert
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
pos=int(input("Enter pos:"))
x=int(input("Enter value:"))
dq.insert(pos,x)
print("After insertion:",dq)
