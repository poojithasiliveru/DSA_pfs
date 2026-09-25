#Doubly Liked List insert at begin and delete at begin
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
print("Doubly Linked List before delete:")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
#Delete at begin
if head is None:
    print("DLL is Empty...")
else:
    head=head.next
    if head is not None:
        head.prev=None
print("Doubly Linked List after delete")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")