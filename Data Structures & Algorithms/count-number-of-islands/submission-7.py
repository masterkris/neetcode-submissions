class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # main idea: traverse from a 1 (given it hasnt been visited before), connected to it horizontally or vertically
        # involves checking neighbors
        # mark as visited as we go to avoid re-counting
        # BFS = queue, pop from queue, do checks, satisfy condition, add to queue

        rows = len(grid)
        cols = len(grid[0])

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        visit = set()
        q = deque()
        islands = 0

        def bfs(r, c):
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visit:
                        q.append((nr, nc))
                        visit.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
       



        