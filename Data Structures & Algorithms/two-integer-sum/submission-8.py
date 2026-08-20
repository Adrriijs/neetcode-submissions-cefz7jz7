class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1.naive solution : try all possible combination

        """
        2. using compliment:
        ex. nums = [3,4,5,6], target = 7

        hashmap:
        7 - 3 = 4 (key), index 0 (value)
        4 is already in map, index 1

        output = [0,1]
        """

        map = {}

        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return[map[nums[i]],i]
