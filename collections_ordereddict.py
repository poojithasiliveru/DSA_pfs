#ordereddict
from collections import OrderedDict
d=OrderedDict()
n=int(input("Enter number of elements:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
print("Ordered Dictionary:",d)