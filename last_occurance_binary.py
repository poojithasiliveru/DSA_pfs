#Find a last occurance of a number using binary search
arr=list(map(int,input("Enter numbers:").split()))
target=int(input("Enter target number:"))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        ans=mid
        high=mid-1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
print("First Occurance:",ans)
