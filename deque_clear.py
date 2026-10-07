#clear
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
dq.clear()
print("After clear:",dq)
