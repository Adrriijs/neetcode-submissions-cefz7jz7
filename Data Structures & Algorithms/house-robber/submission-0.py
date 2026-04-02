class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down

        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
            
            #skip = dp[i-1]
        return dfs(0)