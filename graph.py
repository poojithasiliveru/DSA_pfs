#create a geaph and connecting the vertices
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
for v in graph:
    print(v,"->", graph[v])