class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in hashmap:
                res = [hashmap[nums[i]],i]
            hashmap[target - nums[i]] = i
        
        return res
            