#Types of recursion
'''
1. Direct 
2. In Direct
3. Head
4. Tail
5. Tree -> recursion can be done using multiple functions
6. Nested ->function calling within a function
'''

#Direct Recursion
'''
def numbers(n):
    if n==0:
        print("Done")
        return
    print(n, end=' ')
    numbers(n-1)
n=int(input("Enter n value:"))
numbers(n)
'''
#In Direct Recursion
'''
def even(n):
    if n==0:
        print(copy,"is even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(copy,"is odd")
        return 
    even(n-1)
n=int(input("Enter n value:"))
copy=n
even(n)
'''
#Tree Recutsion
'''
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter n value:"))
for i in range(n):
    print(fib(i), end=' ')
'''
'''
def tree(n):
    if n<=0:
        return 
    print(n, end=' ')
    tree(n-1)
    tree(n-1)
n=int(input("Enter a number:"))
tree(n)
'''

#Head Recursion
def head(n):
    if n==0:
        return 
    head(n-1)
    print(n)
n=int(input("Enter n value:"))
head(n)