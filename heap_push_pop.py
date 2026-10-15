#heap->pushpop-->adding and deleting at a time->least value will be deleted
import heapq
arr=list(map(int,input("Enter elements:").split()))
heapq.heapify(arr)
print("Heapified array:", arr)
value=int(input("Enter value to insert:"))
heapq.heappushpop(arr, value)
print("Array after insertion:", arr)