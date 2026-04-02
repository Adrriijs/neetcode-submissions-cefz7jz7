class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        ans = 0

        while len(nums) >= k:
            ans = heapq.heappop(nums)
        
        return ans