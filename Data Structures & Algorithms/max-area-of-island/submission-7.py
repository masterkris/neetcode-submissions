class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        q = deque()

        dirs = [[-1,0], [1,0], [0,1], [0,-1]]   
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
                    area = 0

                    while q:
                        row, col = q.popleft()
                        area += 1

                        for dr, dc in dirs:
                            nr, nc = row + dr, col + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visit:
                                visit.add((nr, nc))
                                q.append((nr, nc))

                    maxArea = max(area, maxArea)
        
        return maxArea

        