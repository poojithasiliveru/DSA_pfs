#BFS using deque
from collections import deque
n=int(input("Enter number of vertices:"))
e=int(input("Enter number of edges:"))
vertices=input("Enter vertices:").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    u,v=input("Enter edges:").split()
    graph[u].append(v)
    graph[v].append(u)
start=input("Enter staring vertex:")
queue=deque([start])
visited=[start]
while queue:
    node=queue.popleft()
    print(node,end=" ")
    for adj in graph[node]:
        if adj not in visited:
            visited.append(adj)
            queue.append(adj)