class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            local = []
            for subset in res:
                local.append(subset + [num])
            res += local

        return res