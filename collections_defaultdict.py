#default dictionary
from collections import defaultdict
d=defaultdict(int)
n=int(input("Enter number of elements:"))
for i in range(n):
    key=input("Enter key:")
    d[key]+=1
print("Dictionary:",dict(d))