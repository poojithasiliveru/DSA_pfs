#Doubly Liked List insert at begin
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter a value:"))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print("Doubly Linked List:")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")