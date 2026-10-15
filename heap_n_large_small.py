import heapq
arr=list(map(int,input("Enter elements:").split()))
n=int(input("Enter the value of n:"))
print(heapq.nlargest(n,arr))
print(heapq.nsmallest(n,arr))