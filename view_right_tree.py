#right View of a tree
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
            no=queue.pop(0)
            if i==n-1:
                print(no.data, end=' ')
            if no.left:
                queue.append(no.left)
            if no.right:
                queue.append(no.right)
values=list(map(int,input("Enter values:").split()))
root=node(values[0])
queue=[root]
i=1
while queue and i<len(values):
    no=queue.pop(0)
    if values[i]!=-1:
        no.left=node(values[i])
        queue.append(no.left)
    i+=1
    if i<len(values) and values[i]!=-1:
        no.right=node(values[i])
        queue.append(no.right)
    i+=1
left_view(root)