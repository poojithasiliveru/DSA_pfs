#min heap
class minheap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    def heapify_up(self, i):
        while i>0:
            parent=(i-1)//2
            if self.heap[parent]<=self.heap[i]:
                break
            self.heap[parent], self.heap[i]=(self.heap[i], self.heap[parent])
            i=parent
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        minimum=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return minimum
    def heapify_down(self,i):
        n=len(self.heap)
        while True:
            smallest=i
            left=2*i+1
            right=2*i+2
            if left<n and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==i:
                break
            self.heap[i],self.heap[smallest]=(self.heap[smallest],self.heap[i])
            i=smallest
    def get_min(self):
        return self.heap[0]
    def display(self):
        print(self.heap)
h=minheap()
arr=list(map(int,input("Enter elements:").split()))
for x in arr:
    h.insert(x)
h.display()
print("Minimun heap:", h.get_min())
print("Extracted:",h.extract_min())
h.display()

