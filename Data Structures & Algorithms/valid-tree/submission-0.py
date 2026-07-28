class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # DFS
        # Valid tree = fully connected + no cycles

        # n nodes --> n - 1 edges: check
        # build adjacency list
        # run DFS from node 0
        # use visited set
        # if visited node found, cycle exists, return False
        # after DFS, check if all nodes were visited --> connected graph
        # return True if conditions hold

        if len(edges) > (n - 1):
            return False
        
        adj = []

        for i in range(n):
            adj.append([])
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set() # filter out duplicates

        def dfs(node, parent): # keep parent to track which node we came from, not for cycles

        # if we reached already visited node
        # other than parent, there is cycle

            if node in visit:
                return False
            
            visit.add(node) # else add to visit set

            for nei in adj[node]:
                if nei == parent: # if neighbor of node is parent, not counted
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
            # start at node 0, parent -1

            
        