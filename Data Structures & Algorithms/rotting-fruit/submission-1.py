class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        dr = [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]

        while fresh > 0 and q:
            for i  in range(len(q)):
                r,c = q.popleft()
                
                dr = [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]

                for direc in dr:
                    r2,c2 = direc

                    if r2 < 0 or r2 > row-1 or c2 < 0 or c2 > col-1 or grid[r2][c2] != 1:
                        continue
                    
                    q.append((r2,c2))
                    grid[r2][c2] = 2
                    fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1