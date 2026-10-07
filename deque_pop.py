#pop and popleft
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
dq.pop()
print("poped at right:",dq)
dq.popleft()
print("poped at left:",dq)
