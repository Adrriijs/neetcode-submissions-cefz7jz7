class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) != 1:
            s1,s2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            w = -s1+s2
            heapq.heappush(maxHeap, -w)

        return -maxHeap[0]
        
