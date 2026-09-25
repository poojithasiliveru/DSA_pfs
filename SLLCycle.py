#Detect a cycle in the SLL
class node:
    def __init__(self,data):
        self.data=data
        self.next=None     
values =list(map(int,input("Enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]
#create a cyacle with position
cycleposition=int(input("Enter Position to connect the last node:"))
nodes[-1].next=nodes[cycleposition]
#Detect the cycle
x=head=nodes[0]
y=head
while y is not None and y.next is not None:
    x=x.next
    y=y.next.next
    if x==y:
        print("Cycle detected...")
        #Find the startig node of the cycle
        x==head
        while x!=y:
            x=x.next
            y=y.next
        cyclestart=x
        current=cyclestart
        while True:
            print(current.data,end='->')
            current=current.next
            if current==cyclestart:
                print(current.data)
                break
        break
else:
    print("no cycle detected")