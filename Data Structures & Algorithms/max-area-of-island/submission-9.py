class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        area = 0

        def bfs(r,c):
            currentArea = 0
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            while q:
                r, c = q.popleft()
                currentArea += 1
                
                for dr,dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if 0<= nr < row and 0<= nc < col and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 0

            return currentArea
                

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))
        
        return area