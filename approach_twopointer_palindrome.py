#two pointer approach from either sides-> check palindrome or not
arr=list(map(int,input("Enter elements:").split()))
left=0
right=len(arr)-1
found=True
while left<right:
    if arr[left]!=arr[right]:
        found=False
        break
    left+=1
    right-=1
if found:
    print("Palindromic array")
else:
    print("Not Palindromic array")