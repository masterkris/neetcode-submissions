class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # start from a treasure chest
        # work backward to figure out distance

        # declare rows, cols
        # declare directions for neighbors
        # declare queue
        # iterate through the grid, add cells with 0 to the queue
        # while queue, pop. this is going to be a 0 cell.
        # get valid neighbors using dirs that can be traversed (so have value 2147483647) 
        # modify in-place - set these cells equal to grid[r][c] (where we came from) + 1
        # repeat this throughout until we're done

        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))






                
        