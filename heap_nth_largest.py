#nth largest
import heapq
arr=list(map(int,input("Enter elements:").split()))
n=int(input("Enter n:"))
heap=[]
for val in arr:
    heapq.heappush(heap,-val)
for i in range(n-1):
    heapq.heappop(heap)
print("nth largest element:", -heapq.heappop(heap))

'''largest=heapq.nlargest(n,arr)
print("nth largest element:",largest[-1])'''
