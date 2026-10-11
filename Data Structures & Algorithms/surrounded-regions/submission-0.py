class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        visit = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r,c = q.popleft()

                for dr,dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    nr,nc = r + dr, c + dc
                    
                    if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visit and board[nr][nc] == 'O':
                        q.append((nr,nc))
                        visit.add((nr,nc))

        for r in range(row):
            for c in range(col):
                if (r == 0 or r == row - 1 or c == 0 or c == col - 1) and board[r][c] == 'O' and (r,c) not in visit:
                    bfs(r,c)

        for r in range(row):
            for c in range(col):
                if (r,c) not in visit:
                    board[r][c] = 'X'