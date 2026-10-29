#max heap
import heapq
heap=[]
heapq.heappush(heap,-30)
heapq.heappush(heap,-10)
heapq.heappush(heap,-50)
heapq.heappush(heap,-20)
print([-x for x in heap])
print("Maximum:", -heap[0])
heapq.heappop(heap)
print([-x for x in heap])