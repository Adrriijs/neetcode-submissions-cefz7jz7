class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:                 # template
            mid = lo + (hi - lo) // 2   # template

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

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