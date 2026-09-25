#reverse a Single Linked List
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
values=list(map(int,input("Enter values:").split()))
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=newnode
#reversal
previous=None
current=head
while current is not None:
    nextnode=current.next
    current.next=previous
    previous=current
    current=nextnode
head=previous
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print("Tail")