#linear data structures
#Arrays
'''
1.create and display
2.insert
3.delete
4.append
5.remove
'''

#1.create and display
'''
arr=list(map(int,input("Enter elemets:").split()))
print(arr)
print(*arr)  #used to unpack the data
'''

#2.accessing an element with index value
'''
arr=list(map(int,input("Enter elemets:").split()))
index=int(input("Enter a value:"))
print("Element",arr[index])
print(arr)
'''
#create and insert an element print array
'''
arr=list(map(int,input("Enter elements:").split()))
index=int(input("Enter index:"))
value=int(input("Enter value to be inserted:"))
arr.insert(index,value)
print(arr)
arr.append(value)
print(arr)
'''
#create and pop the element
'''
arr=list(map(int,input("Enter elements:").split()))
value=int(input("Enter value to be deleted:"))
arr.remove(value)
print(arr)
index=int(input("Enter index:"))
arr.pop(index)
print(arr)
'''

#searching an element & return index value in an array
'''
arr=list(map(int,input("Enter elements:").split()))
print(arr)
value=int(input("Enter the value to be searched:"))
found=0
for i in range(len(arr)):
    if arr[i]==value:
        found=True
        print(value,"found at index",i)
        break
else:
    print("Element not found...")
'''

#find minimum
'''
arr=list(map(int,input("Enter Elements:").split()))
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min=arr[i]
        print("The minimum element is:",min)
'''

#sort the lements
'''
arr=list(map(int,input("Enter Elements:").split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
'''
#another to sort the elements
arr=list(map(int,input("Enter Elements:").split()))
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)