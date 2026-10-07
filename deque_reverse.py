#reverse
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
dq.reverse()
print("Reversed:",dq)