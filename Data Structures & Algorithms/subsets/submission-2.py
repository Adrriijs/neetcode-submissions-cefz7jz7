class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #base case
        res = []
        subset = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision one
            subset.append(nums[i])
            dfs(i + 1)

            # decision two
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

"""
[1,2]

res = [[1,2]]

subset = []

dfs(0) -> 1
"""