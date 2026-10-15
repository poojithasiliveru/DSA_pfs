#DFS 
n=int(input("Enter number of nodes:"))
nodes=input("Enter nodes:").split()
graph={}
for node in nodes:
    graph[node]=input(f"Enter neighbours of {node}:").split()
start=input("Enter starting node:")
visited=set()
def dfs(node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for adj in graph[node]:
            dfs(adj)
dfs(start)