#heap->replace->replaces the peek element with new elemwnt
import heapq
arr=list(map(int,input("Enter elements:").split()))
heapq.heapify(arr)
print("Heapified array:", arr)
value=int(input("Enter value to replace:"))
heapq.heapreplace(arr, value)
print("Array after replacement:", arr)