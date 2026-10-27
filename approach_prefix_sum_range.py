#Prefix range sum
arr=list(map(int,input("Enter elements:").split()))
prefix=[arr[0]]
for i in range(len(arr)):
    prefix.append(prefix[i-1]+arr[i])
start=int(input("Enter staring index:"))
end=int(input("Enter ending index:"))
if start==0:
    print(prefix[end])
else:
    print(prefix[end]-prefix[start-1])