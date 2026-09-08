class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dirs = [[-1,0], [0,1], [1,0], [0,-1]]

        q = deque()
        seen = set()
        islands = 0

        def bfs(r, c):
           seen.add((r,c))
           q.append((r,c))

           while q:
              row, col = q.popleft()

              for dr, dc in dirs:
                  r, c = row + dr, col + dc

                  if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))
        

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands

            
        