#min heap
import heapq
heap=[]
heapq.heappush(heap,30)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,5)
print(heap)
print("Minimum:",heap[0])
heapq.heappop(heap)
print(heap)