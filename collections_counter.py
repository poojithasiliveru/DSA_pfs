#counter
from collections import Counter 
nums=input("Enter numbers:").split()
c=Counter(nums)
print("Counter:",c)

#Most common counter
print(c.most_common(1))