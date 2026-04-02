class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        row = len(grid)
        col = len(grid[0])
        counter = 0

        def bfs(r,c):
            nonlocal counter
            q.append((r,c))

            while q:
                r,c = q.popleft()
                
                dr = [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]

                for direc in dr:
                    r2,c2 = direc

                    if r2 < 0 or r2 > row-1 or c2 < 0 or c2 > col - 1 or grid[r2][c2]=="0":
                        continue

                    q.append((r2,c2))
                    
                    grid[r2][c2] = "0"

            counter += 1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)
                
        
        return counter

            