'''#sliding window approach
arr=list(map(int,input("Enter values: ").split()))
k=int(input("Enter slide size: "))
windowsum=sum(arr[:k])
max_sum=windowsum
for i in range(k,len(arr)):
    windowsum=windowsum+arr[i]-arr[i-k]
    if windowsum>max_sum:
        max_sum=windowsum
print("Maximum sum: ",max_sum)'''

#sliding window approach on each side
arr=list(map(int,input("Enter values: ").split()))
k=int(input("Enter slide size: "))
for i in range(len(arr)-k+1):
    print(sum(arr[i:i+k]))