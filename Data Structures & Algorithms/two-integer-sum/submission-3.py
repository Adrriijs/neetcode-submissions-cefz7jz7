class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        answer = []

        for i in range (len(nums)):
            holder = target - nums[i]
            if holder in hashmap:
                answer.append(hashmap[holder])
                answer.append(i)
            else:
                hashmap[nums[i]] = i

        return answer