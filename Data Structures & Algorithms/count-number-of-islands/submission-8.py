class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visit = set()
        islands = 0
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        def bfs(r, c):
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands
        