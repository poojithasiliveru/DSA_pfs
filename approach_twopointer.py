#Two pointer approach from either sides
arr=list=list(map(int,input("Enter elements:").split()))
target=int(input("Enter target:"))
arr.sort()
left=0
right=len(arr)-1
while left<right:
    total=arr[left]+arr[right]
    if total==target:
        print(arr[left], arr[right])
        break
    elif total<target:
        left+=1
    else:
        right-=1
else:
    print("Target not found")
