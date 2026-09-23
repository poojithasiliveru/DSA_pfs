#Delete a value at a position
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
pos=int(input("Enter the position to delete:"))
newnode=node(value)
if head is None:
    print("SLL Empty...")
elif pos==1:
    head=head.next
else:
    current=head
    for i in range(pos-2):
        current=current.next
    current.next=current.next.next
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print("Tail")