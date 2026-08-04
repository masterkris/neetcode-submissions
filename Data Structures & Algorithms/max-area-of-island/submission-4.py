class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # BFS approach

        # everytime we see a 1, we can start computing area using neighbors. if neighbors are 1, we can add to the area.

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visit = set()
        q = deque()
        max_area = 0

        def bfs(r, c):
            visit.add((r,c))
            q.append((r,c))

            area = 1 # count starting cell

            while q:
                row, col = q.popleft()

                dirs = [[-1,0],[1,0],[0,1],[0,-1]]

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
                    max_area = max(max_area, bfs(r,c))
        
        return max_area
                
        