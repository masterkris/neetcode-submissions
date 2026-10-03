class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # adjacency list
        # go both ways, map from node to next node in both dirs.
        # visited set
        # dfs function
        # don't have any more nodes left to visit, so we're done exploring that connected component
        # this would happen when already in visited
        # increment (outside loop) when you start new DFS from unvisited node, next one in edges list

        adj = [[] for _ in range(n)]

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei) # already accounting for return
        
        connected = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                connected += 1
        
        return connected


        