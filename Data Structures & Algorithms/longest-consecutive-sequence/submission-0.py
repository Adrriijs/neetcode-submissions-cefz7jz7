class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        dont focus on saving the sequence, because they only ask the length

        idea:
        1. cehck for starting sequence
        2. if the next num is +1 from initial at that point then length += 1
        """
        s = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s:
                length = 1

                while (num + length) in s:
                    length += 1

                longest = max(length, longest)
        
        return longest