from typing import List
import heapq

li = [3,5,2,1,3,4]
heapq.heapify(li) 
print(li) #[1, 3, 2, 5, 3, 4]

li = [3,5,2,1,3,4]

h = []
for item in li:
    heapq.heappush(h, item)

print(h) # [1, 2, 3, 5, 3, 4]

def findKthLargest(nums: List[int], k:int) -> int:
    h = []

    for n in nums:
        heapq.heappush(h, n*-1)

    for _ in range( k -1 ):
        heapq.heappop(h)

    return h[0] * -1

class MaxHeap:
    def __init__(self, items=[]):
        self.h = [x*-1 for  x in items]        
        if items:
            heapq.heapify(self.h)

    def __len__(self):
        return len(self.h)
    
    def push(self, item):
        heapq.heappush(self.h,  -1*item)

    def pop(self):
        return -heapq.heappop(self.h)

    def look(self):
        return -1*self.h[0]
    
if __name__ == "__main__":
    items=[1,3,5,7,9,2,4,6,8,0]
    mx_heap = MaxHeap()
    for item in items:
        mx_heap.push(item)

    print(mx_heap.look())

    li = [mx_heap.pop() for _ in range(len(mx_heap))]

    print(li)