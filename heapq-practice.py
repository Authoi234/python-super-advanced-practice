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
