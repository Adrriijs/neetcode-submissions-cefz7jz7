class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
        # [-4,-1,-1,0,1,2]
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]: # check next a duplicate atau gk
                continue
            
            else:
                l, r = i + 1, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] == -a:
                        res.append([a, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    elif nums[l] + nums[r] > -a: # too big
                        r -= 1
                    else:
                        l += 1
        
        return res

        