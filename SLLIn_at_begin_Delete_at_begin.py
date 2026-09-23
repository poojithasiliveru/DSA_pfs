#Single Linked List insert at begin and Delete at begin
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
print("SLL Before Deletion")
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')
if head is None:
    print("SLL is Empty...")
else:
    head=head.next
print("SLL After Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')