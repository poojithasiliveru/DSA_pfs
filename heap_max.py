# Max Heap
class maxheap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] >= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = (self.heap[i], self.heap[parent])
            i = parent
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return maximum
    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i], self.heap[largest] = (self.heap[largest], self.heap[i])
            i = largest
    def get_max(self):
        return self.heap[0]
    def display(self):
        print(self.heap)
h = maxheap()
arr = list(map(int, input("Enter elements: ").split()))
for x in arr:
    h.insert(x)
h.display()
print("Maximum element:", h.get_max())
print("Extracted:", h.extract_max())
h.display()