class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                
                for dr,dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
                
            time += 1
            
        if fresh == 0:
            return time
        else:
            return -1
