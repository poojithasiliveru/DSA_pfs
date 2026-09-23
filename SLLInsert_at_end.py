#Single Linked List insert at end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values =list(map(int,input("Enter elements:").split()))
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')