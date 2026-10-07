#count
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
x=int(input("Enter value:"))
print("Count:",dq.count(x))