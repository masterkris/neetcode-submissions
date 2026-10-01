class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # if two nodes already belong to the same connected component, adding an edge between them must create a cycle

        # Union-Find
        # Make parent array
        # Each node starts as its own parent

        # find(x):
        # figure out which component x belongs to
        # if x is not its own parent, find root/src of its parent
        # make x point directly to that root
        # return root 
        # so main idea is to find source of each node

        # for each edge (a,b):
        # find root of a
        # find root of b
        # if roots are the same, return [a,b] as edge creates cycle
        # otherwise connect the two components
        # Time: O(n), space: O(n)

        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for a, b in edges:
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a,b]
            
            parent[rootA] = rootB


        