class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # DFS to count components
        # everytime we start DFS from unvisited node, we begin new component
        
        # adjacency list
        # visited array
        # declare components 
        # for each node, if not visited, run DFS
        # increment components by 1
        # return components
        # Time: O(V + E)
        # Space: O(V + E)

        adj = [[] for _ in range(n)]

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visit = set()

        components = 0

        def dfs(node):

            visit.add(node)
            
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                components += 1
                
        return components

        