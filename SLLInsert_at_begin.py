#Single Linked List insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
values =list(map(int,input("Enter elements:").split()))
for value in values:
    newnode=node(value)
    newnode.next=head
    head=newnode
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')