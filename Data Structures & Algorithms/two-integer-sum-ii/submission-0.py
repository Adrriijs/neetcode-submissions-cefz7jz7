class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers) - 1

        while l < r:
            calculation = numbers[l] + numbers[r]
            if calculation == target:
                res = [l +1  ,r + 1]
                break
            elif calculation > target:
                r -= 1
            else:
                l += 1

        return res

