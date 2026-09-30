#Circuler Linked List traversal by position
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
values=list(map(int,input("Enter elements:").split()))
head=None
tail=None
for value in values:
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
tail.next=head
pos=int(input("Enter position:"))
current=head
for i in range(pos-1):
    current=current.next
print("Traversal:")
temp=current
while True:
    print(temp.data,end=' ')
    temp=temp.next
    if temp==current:
        break