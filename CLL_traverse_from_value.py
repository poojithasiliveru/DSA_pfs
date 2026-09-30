#Circuler Linked List traverse from value
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
start=int(input("Enter the starting node:"))
current=head
while current.data!=start:
    current=current.next
    if current==head:
        print("Vlaue not found")
        exit()
temp=current
print("Traversal:")
while True:
    print(temp.data,end=' ')
    temp=temp.next
    if temp==current:
        break