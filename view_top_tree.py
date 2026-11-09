class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def top_view(root):
    if root is None:
        return
    queue=[(root,0)]
    result={}
    while queue:
        node,hd=queue.pop(0)
        if hd not in result:
            result[hd]=node.data
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    for hd in sorted(result):
        print(result[hd], end=' ')
values=list(map(int,input("Enter elements:").split()))
root=Node(values[0])
queue=[root]
i=1
while queue and i<len(values):
    node=queue.pop(0)
    if values[i]!=-1:
        node.left=Node(values[i])
        queue.append(node.left)
    i+=1
    if i<len(values) and values[i]!=-1:
        node.right=Node(values[i])
        queue.append(node.right)
    i+=1
top_view(root)