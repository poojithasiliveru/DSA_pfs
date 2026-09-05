#Constant Time Complexity
'''
n=int(input("Enter a number:"))
print("Number:",n)'''   #T.C=O(1) ,S.C=O(1)->return only one value

#Linear time complexity
'''
n=int(input("Enter a number:"))
for i in range(n):
    print(i,"Poojitha",end=' ')   #T.C=O(n) ,S.C=O(2)->each time returns 2 values
'''

#Quadratic Time Complexity
'''
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        print(i,j, end=' ')   #T.C=O(n^2) ,S.C=O(2)
    print()
'''
'''
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j, end=' ')   #T.C=O(n^3) ,S.C=O(3)
    print()
'''

'''
n=int(input("Enter n:"))
for i in range(n):
    print("😎", end=' ')
for j in range(n):
    print("🤩", end=' ')
print()                        #T.C=2n ,S.C=O(1)
'''

'''
n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        print("😊",end=' ')
    for k in range(n):
        print("😂",end=' ')
    print()                    #T.C=2*(n^2), S.C=O(n)
print()
'''

#Logarithmic Time Complexity
'''
n=int(input("Enter n:"))
while n>1:
    print(n)
    n//=2                     #T.C=O(log n), S.C=O(1)
'''

import math
n=int(input("Enter n:"))
while n>2:
    print(n)
    n=math.sqrt(n)            #T.C=O(log(log(n)))