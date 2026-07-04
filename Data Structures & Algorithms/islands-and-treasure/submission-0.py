class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
             if (r == rows or c == cols or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == -1):
                return
            
             visit.add((r,c))
             q.append([r,c])
        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)): # next level
                r, c = q.popleft()
                grid[r][c] = dist # distance to nearest treasure
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        