#print a Pyramid
n=int(input("Enter n value:"))
for i in range(1,n+1):
    print(" "*(n-i), end=' ')
    print("* "*i)
