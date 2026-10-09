#create a tree and access a tree -> preorder traversal
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
arr=list(map(int,input("Enter elements:").split()))
nodes=[]
for val in arr:
    nodes.append(node(val))
for i in range(len(nodes)):
    left=2*i+1
    right=2*i+2
    if left < len(nodes):
        nodes[i].left=nodes[left]
    if right<len(nodes):
        nodes[i].right=nodes[right]
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
print("Pre-Order traversal")
preorder(nodes[0])

