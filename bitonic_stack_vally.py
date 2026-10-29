arr=list(map(int,input("Enter elements:").split()))
arr.sort()
left=arr[::-2]
right=arr[1::2]
print("Vally:",*(left+right))