#vertical order travrsal
from collections import deque
arr=input("Enter elements:").split()
q=deque([(0,0)])
columns={}
while q:
    index, col=q.popleft()
    if index>=len(arr):
        continue
    columns.setdefault(col, []).append(arr[index])
    q.append((2*index+1, col-1))
    q.append((2*index+2, col+1))
for col in sorted(columns):
    print(*columns[col])
