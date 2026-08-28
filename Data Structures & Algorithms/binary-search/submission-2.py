class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
            else:
                return mid

        return -1

        """
        -1,0,2,4,6,8

        target 4

        lo -1
        hi 8
        mid 2 != 4

        lo 4
        hi 8
        mid 6 != 4

        lo 4
        hi 6
        mid 4
        """