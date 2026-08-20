class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """
        ex: 1,2,3,3

        len = 4
        set = 1,2,3
        len(set) = 3

        so its duplicate -> true
        """
        
        return len(nums) != len(set(nums))