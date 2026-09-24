class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        dirs = [[-1,0],[1,0], [0,1], [0,-1]]
        q = deque()
        maxArea = 0

        def bfs(r, c):
            seen.add((r,c))
            q.append((r,c))
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    maxArea = max(bfs(r,c), maxArea)
        
        return maxArea


        

