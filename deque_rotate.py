#rotate-clockwise and anti-clockwise

from collections import deque
dq=deque(map(int,input("Enter values:").split()))
print(dq)
x=int(input("Enter value to rotate:"))
dq.rotate(x)
print("Clockwise Rotation:",dq)
y=int(input("Enter value to rotate:"))
dq.rotate(-y)
print("Anti-clockwise Rotation:",dq)