class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        row = len(grid)
        col = len(grid[0])
        area = 0

        def bfs(r,c):
            nonlocal area
            q.append((r,c))
            grid[r][c] = 0

            counter = 0

            while q:
                r,c = q.popleft()
                counter += 1

                dr = [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]


                for direc in dr:
                    r2, c2 = direc

                    if r2 < 0 or r2 > row - 1 or c2< 0 or c2>col-1 or grid[r2][c2] == 0:
                        continue
                    
                    q.append((r2,c2))
                    grid[r2][c2] = 0


                    
            area = max(area, counter)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    bfs(r,c)
        
        return area

