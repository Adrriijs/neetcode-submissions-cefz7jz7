class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        9 5 4 2 3 3 7 9 10 9
        remove 9 -> bigger than 1
        remove 4 -> bigger 2
        remove 3 -> duplicate

        123412345

        length = 0

        if [char] > [char +1] -> remove [char]

        9 1 5 4
        """
        memo = [None] * len(nums)

        def dfs(i):
            
            if memo[i]:
                return memo[i]

            length = 1
            
            for n in range(i +1, len(nums)):
                if nums[i] < nums[n]:
                    length = max(length, 1 + dfs(n))

            memo[i] = length

            return memo[i]
                
        return max(dfs(i) for i in range(len(nums)))