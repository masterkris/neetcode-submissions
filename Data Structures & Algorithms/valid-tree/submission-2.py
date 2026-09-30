class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # condition: no cycle (use set to track) and edges = n - 1
        # adjacency list

        # visit set

        # dfs function --> using curr. node and parent
        # if already visited, return False
        # else add to visit set
        # go through neighbors in node
        # only acceptable neighbor is parent
        # else its not a tree
        # return dfs(0,-1) and make sure visit's length is n
        
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        visit = set()
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
    

        