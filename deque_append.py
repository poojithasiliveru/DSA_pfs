#append
from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
val=int(input("Enter value: "))
dq.append(val)
print("Appended at right:",dq)
val2=int(input("Enter value:"))
dq.appendleft(val2)
print("Appended at left:",dq)