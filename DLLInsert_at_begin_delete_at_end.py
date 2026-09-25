#Doubly Liked List insert at begin and delete at end
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
print("Doubly Linked List before delete")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
#Delete at end
if head is None:
    print("DLL Empty...")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.prev.next=None
print("Double Linked Linst After delete")
temp=head
while temp is not None:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")