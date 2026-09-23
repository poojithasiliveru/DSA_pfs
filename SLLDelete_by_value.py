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
value=int(input("Enter the value to delete:"))
if head is None:
    print("SLL Empty...")
elif head.data==value:
    head=head.next
else:
    current=head
while current is not None:
    if current.next.data==value:
        current.next=current.next.next
        break
    current=current.next
current=head
while current is not None:
    print(current.data, end='->')
    current=current.next
print("Tail")