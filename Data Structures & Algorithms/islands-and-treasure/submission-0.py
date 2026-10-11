class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(q):
            step = 0
            while q:
                step += 1
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == INF:
                            grid[nr][nc] = step
                            q.append((nr, nc))

        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))

        bfs(q)