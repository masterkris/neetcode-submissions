class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Main Idea:
        # BFS
        # find rotten fruits and work backward

        # declare queue, directions for neighbors, and how many fresh fruits there are
        # iterate through grid
        # add rotten to queue
        # add fresh to tally

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        fresh = 0
        mins = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        # while queue not empty, pop (rotten)
        # check neighbors and if they're valid
        # if not rotten, make rotten
        # add to queue
        # increment mins 

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                
            mins += 1

        # return mins if fresh == 0, else -1
        return mins if fresh == 0 else -1






        