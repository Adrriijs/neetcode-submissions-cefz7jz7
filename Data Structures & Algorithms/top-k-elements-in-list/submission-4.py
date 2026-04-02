class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range (len(nums) +1)]
        answer = []

        count = Counter(nums)
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)

                if len(answer) == k:
                    return answer
            
        
        return answer
