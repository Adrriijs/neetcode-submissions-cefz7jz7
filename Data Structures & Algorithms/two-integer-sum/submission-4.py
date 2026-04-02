class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        ans = []

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                ans = [hashmap[diff], i]
                break
            
            hashmap[nums[i]] = i
        
        return ans

        