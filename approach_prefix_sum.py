#Prefix sum
arr=list(map(int,input("Enter elements:").split()))
prefix=[]
total=0
for num in arr:
    total+=num
    prefix.append(total)
print("Prefix Sum:", prefix)