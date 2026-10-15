#DFS 
n=int(input("Enter number of nodes:"))
nodes=input("Enter nodes:").split()
graph={}
for node in nodes:
    graph[node]=input(f"Enter neighbours of {node}:").split()
visited=set()
def dfs(node):
    print(node,end=' ')
    visited.add(node)
    for adj in graph[node]:
        if adj not in visited:
            dfs(adj)
    print("Backtracking from", node)   #Backtracking
start=input("Enter starting node:")
dfs(start)