#heap
import heapq
arr=list(map(int,input("Enter elements:").split()))
heapq.heapify(arr)
print("Heapified array:", arr)
value=int(input("Enter value to insert:"))
heapq.heappush(arr, value)
print("Array after insertion:",arr)
heapq.heappop(arr)
print("Array after deletion:", arr)
