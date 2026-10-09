#create a tree and access a tree -> in order traversal
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
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
print("In-Order traversal")
inorder(nodes[0])

