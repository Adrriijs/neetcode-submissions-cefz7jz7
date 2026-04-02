class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # max area

        # count part of island (block 1)
        # i will save the max area

        # dfs and then keep counting the area
        max_a = 0
        directions = [(1,0), (-1,0), (0,1),(0,-1)]

        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            
            grid[r][c] = 0
            area = 1
            
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_a = max(max_a, dfs(r,c))

        return max_a