class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0
        time = 0
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        # initialize queue with positions of all rotten oranges
        # count total number of fresh oranges

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        

        dirs = [[0, 1], [0, -1], [1,0], [-1,0]]

        # while queue not empty and fresh oranges are there in grid
        # process all nodes in queue
        # check 4 neighbors for each rotten orange, check that it is withon bounds.
        # if neighbor fresh, make it rotten. decrease fresh count and add to queue.
        # increment time by 1
        # then return

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc

                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2 # now rotten
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


        