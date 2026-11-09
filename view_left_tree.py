#left View of a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def left_view(root):
    if root is None:
        return 
    queue=[root]
    while queue:
        n=len(queue)
        for i in range(n):
            n=queue.pop(0)
            if i==0:
                print(n.data, end=' ')
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
values=list(map(int,input("Enter values:").split()))
root=node(values[0])
queue=[root]
i=1
while queue and i<len(values):
    n=queue.pop(0)
    if values[i]!=-1:
        n.left=node(values[i])
        queue.append(n.left)
    i+=1
    if i<len(values) and values[i]!=-1:
        n.right=node(values[i])
        queue.append(n.right)
    i+=1
left_view(root)