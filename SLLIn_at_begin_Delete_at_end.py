#Single Linked List insert at begin and Delete at end
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
print("SLL Before Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')
if head is None:
    print("SLL is Empty...")
elif head.next is None:
    head=None
else:
    current=head
    while current.next.next is not None:
        current=current.next
    current.next=None 
print("SLL After Deletion")
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('Tail')