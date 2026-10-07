#remove
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
x=int(input("Enter value to remove:"))
x=dq.remove(x)
print("Removed element:",x)
print("After Remove:",dq)