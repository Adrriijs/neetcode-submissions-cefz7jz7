class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis = []

        for x,y in points:
            dis.append([x**2 + y**2, x, y])

        heapq.heapify(dis)

        ans = []

        while k > 0:
            dist, x, y = heapq.heappop(dis)
            ans.append([x,y])
            k -= 1

        return ans