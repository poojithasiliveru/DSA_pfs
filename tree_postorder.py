#create a tree and access a tree ->post order traversal
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
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')
print("Post-Order traversal")
postorder(nodes[0])