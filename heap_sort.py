#heap-->sort
import heapq
arr=list(map(int,input("Enter elements:").split()))
heapq.heapify(arr)
result=[]
while arr:
    result.append(heapq.heappop(arr))
print("The sorted elements are:", result)