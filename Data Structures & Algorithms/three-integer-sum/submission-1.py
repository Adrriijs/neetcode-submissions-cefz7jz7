class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        a+b+c = 0
        b+c = -a
        """
        res = []
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i + 1, len(nums) - 1

            while l < r:
                comp = nums[l] + nums[r]
                if comp > -nums[i]:
                    r -= 1
                elif comp < -nums[i]:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res