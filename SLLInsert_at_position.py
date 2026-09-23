#SLL Insert a value at position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
values=list(map(int,input("Enter Elements:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
value=int(input("Enter value to insert:"))
pos=int(input("Enter position:"))
newnode=node(value)
if pos==1:
    newnode.next=head
    head=newnode
else:
    current=head
    for i in range(pos-2):
        current=current.next
    newnode.next=current.next
    current.next=newnode
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print("Tail")