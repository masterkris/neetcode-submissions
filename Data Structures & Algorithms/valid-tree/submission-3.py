class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # no cycle, edges = n - 1
        # neighbor, adjacent node can only be from parent

        # adjacency list and visit set
        # undirected, goes both ways
        # dfs function (node, parent)
        # if visited, cycle, so False
        # add node to visited
        # if not visited, check the neighbors
        # if neighbor is parent, continue
        # else return False

        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        visit = set()
        
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False
        
            return True

        return dfs(0, -1) and len(visit) == n
        

        