class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        paci = set()
        atla = set()
        res = []

        def pac(r,c):
            if (r,c) in paci:
                return
            
            paci.add((r,c))

            dr = [(r,c-1), (r, c+1), (r-1,c), (r+1,c)]
            
            for direc in dr:
                r2,c2 = direc

                if r2 <0 or r2 > row-1 or c2 <0 or c2>col-1 or heights[r][c] > heights[r2][c2]:
                    continue

                pac(r2,c2)

        def atl(r,c):
            if (r,c) in atla:
                return

            atla.add((r,c))

            dr = [(r,c-1), (r, c+1), (r-1,c), (r+1,c)]
            
            for direc in dr:
                r2,c2 = direc

                if r2 <0 or r2 > row-1 or c2 <0 or c2>col-1 or heights[r][c] > heights[r2][c2]:
                    continue

                atl(r2,c2)

        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    pac(r,c)
                if r == row - 1 or c == col-1:
                    atl(r,c)

        return list(paci & atla)