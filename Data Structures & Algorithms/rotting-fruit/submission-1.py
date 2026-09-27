class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        mins = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # count fresh
                    fresh += 1
                if grid[r][c] == 2: # start from rotten
                    q.append((r,c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc)) # now infected, so append
                        fresh -= 1
            
            mins += 1
        
        return mins if fresh == 0 else -1





        