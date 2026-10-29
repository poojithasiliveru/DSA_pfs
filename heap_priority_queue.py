#Priority Queue
import heapq
pq=[]
heapq.heappush(pq,(2,"FollowUp"))
heapq.heappush(pq,(1,"Emergency"))
heapq.heappush(pq,(3,"Consultancy"))
while pq:
    priority, task=heapq.heappop(pq)
    print(priority,task)