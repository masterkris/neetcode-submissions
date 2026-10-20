class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # for each neighbor water -> add 1
        # for each neighbor out of bounds -> add 1
        # can be both for a cell
        # look at diagram
        # bfs, find connected 1s

        perimeter = 0

        q = deque()
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        def bfs(r, c):
            nonlocal perimeter
            seen.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        perimeter += 1
                    
                    elif grid[nr][nc] == 0:
                        perimeter += 1

                    elif (nr, nc) not in seen and grid[nr][nc] == 1:
                        
                        q.append((nr, nc))
                        seen.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    bfs(r,c)
        
        return perimeter
        