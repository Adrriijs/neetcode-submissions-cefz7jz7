class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        idea is bucket sort here, bucket per freq

        max freq is the len of arr (nums)

        example:
        1,2,2,3,3,3
        
        bucket sort:
        1: 1
        2: 2
        3: 3

        k = 2 so we take bucket freq 2 and 3

        so count first and then reverse
        """

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k:
                    return res