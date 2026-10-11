class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(x*x + y*y, x, y) for x,y in points]
        heapq.heapify(minHeap)
        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res