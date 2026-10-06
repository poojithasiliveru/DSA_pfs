#chanmap
from collections import ChainMap
d1={}
d2={}
n=int(input("Enter number of elements in d1:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d1[key]=value
n=int(input("Enter number of elements in d2:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d2[key]=value
c=ChainMap(d1,d2)
print("First Data:",d1)
print("Second Data:",d2)
print("ChainMap:",c)