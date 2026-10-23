#two pointer approch from either sides find the middle element of an array
arr=list(map(int,input("Enter elements:").split()))
slow=0
fast=0
arr.sort()
while fast<len(arr)-1 and fast+1<len(arr):
    slow+=1
    fast+=2
print("Middle element:",arr[slow])
