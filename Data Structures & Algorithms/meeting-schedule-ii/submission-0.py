"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
0 ---|----|-----|--------|-- 40
     5----10.   15-------20
meeting room = 1 + 1 = 2 - 1 = 1 + 1 = 2 - 1 = 1 -1 = 0
take max (meeting room) = 2

0 ---|-----|---------|--40
     5-----10
           10 ------ 20
meeting room = 1 + 1 = 2 - 0 = 2 - 1 = 1 - 1 = 0
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s, e = 0, 0
        count = 0
        meet_r = 0

        # 0 5 10
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
                meet_r = max(meet_r, count)
            elif start[s] > end[e]:
                count -= 1
                e += 1
            else: # s == e
                s += 1
                e += 1
        
        return meet_r


            
