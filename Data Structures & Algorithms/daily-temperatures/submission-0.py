class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        if the next bigegr then pop and calculate the index dif -> insert to res

        save the index straight away
        """
        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                prev_i, prev_t = stack.pop()
                res[prev_i] = i - prev_i
            stack.append([i,t])
            

        return res

            