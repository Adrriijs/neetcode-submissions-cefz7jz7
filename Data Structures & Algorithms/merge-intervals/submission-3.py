class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1 - 3
        1 - - - 5
                  6 - 7
        """
        intervals.sort()
        output = [intervals[0]]

        for start,end in intervals:
            lastEnd = output[-1][-1]

            if start <= lastEnd:
                output[-1][-1] = max(lastEnd, end)
            else:
                output.append([start,end])
        
        return output

