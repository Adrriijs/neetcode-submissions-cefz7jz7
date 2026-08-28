class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        idea of prefix and postfix

        example:
        1,2,4,6
        prefix = 1,2,8,24
        postfix = 48,48,24,6

        res = left and right of the number
        res = 48,24,12,8
        """
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res