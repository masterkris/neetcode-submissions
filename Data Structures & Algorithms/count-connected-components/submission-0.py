class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # can use DFS to count components
        # everytime we start DFS from a unvisited node
        # we have found new component

        # Plan:
        # build adjacency list from edges
        # visited array to track visited notes
        # components = 0
        # for each node from 0 to n - 1,
        # if node not visited, run DFS (explore deeply and mark all reachable nodes as visited)
        # increment components by 1
        # return components

        adj = []

        for i in range(n):
            adj.append([])
        
        visit = n * [False]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        components = 0

        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei) 
        

        res = 0
        for node in range(n): 
            if visit[node] == False: # belongs to new component
                visit[node] = True
                dfs(node) # explore neighbors
                res += 1
        return res

        

        