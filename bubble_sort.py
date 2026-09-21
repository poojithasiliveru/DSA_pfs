#Bubble sort

a=list(map(int,input("Enter the numbers:").split()))
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Sorted array:",*a)


