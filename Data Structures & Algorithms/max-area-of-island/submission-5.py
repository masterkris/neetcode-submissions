class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        q = deque()
        maxArea = 0
        dirs = [[-1,0], [1,0], [0,1],[0,-1]]

        def bfs(r, c):
            q.append((r,c))
            visit.add((r,c))

            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
                        area += 1
                
            return area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, bfs(r,c))
            
        return maxArea

        