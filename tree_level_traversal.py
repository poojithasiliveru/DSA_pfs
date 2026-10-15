#level order traversal
from collections import deque
arr=input("Enter elements:").split()
q=deque([0])
while q:
    size=len(q)
    for i in range(size):
        index=q.popleft()
        print(arr[index], end=' ')
        left=2*index+1
        right=2*index+2
        if left<len(arr):
            q.append(left)
        if right<len(arr):
            q.append(right)
    print()
