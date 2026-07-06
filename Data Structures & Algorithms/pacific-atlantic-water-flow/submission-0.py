class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # figure out if cell can reach BOTH Pacific and Atlantic oceans

        # idea: start from the ocean and start from those node bordering it
        # and work inward --> cell of equal OR increasing heights (since flipped)

        # O(n * m)
        # want to search deeply from a node --> DFS

        # visit set to find nodes that are reachable from both oceans

        rows = len(heights)
        cols = len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight): # visit set

            if r < 0 or c < 0 or (r, c) in visit or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols): # for left and right borders
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        for r in range(rows): # for top and bottom borders
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        
        # now compute overlap

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res






        