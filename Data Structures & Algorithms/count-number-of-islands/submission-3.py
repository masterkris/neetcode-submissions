class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

    # edge case: if grid null, return 0 
    # declare rows, cols, visit set, islands var. 
    # we can do a BFS, going layer by layer 
    # declare BFS function taking in (r, c)
    # also declare deque()
    # add to visit set and queue 
    # while q is not empty, pop row, col 
    # declare all 4 dirs
    # add dirs to the row, col instance we popped
    # this checks adjacent neighbors
    # make sure its in range and grid[r][c] == "1" and we haven't visited yet
    # if not, append to queue and visited 

    # now we have BFS done
    # iterate through grid and if we find a 1 and haven't visited yet, run BFS. we have found a new island in this case. and then increment islands by 1.

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()
        islands = 0

        def bfs(r, c):
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                
                dirs = [[-1,0],[1,0],[0,-1],[0,1]]
                
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
    
        return islands

        