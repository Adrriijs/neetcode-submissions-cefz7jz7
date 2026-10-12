class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        print(nums)

        for num in nums:
            if nums[num] > 1:
                return True
            
        return False