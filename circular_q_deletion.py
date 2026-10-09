#circular queue - Delete operation
arr=list(map(int,input("Enter elements:").split()))
value=int(input("Enter value to delete:"))
if value in arr:
    arr.remove(value)
    print("After deletion:",arr)
else:
    print("value not found")