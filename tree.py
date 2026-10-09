#create a tree and access a tree
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
print("Root:",nodes[0].data)
print("Left:",nodes[0].left.data)
print("Right:",nodes[0].right.data)
print("Left.left:",nodes[0].left.left.data)
print("Left.right:",nodes[0].left.right.data)