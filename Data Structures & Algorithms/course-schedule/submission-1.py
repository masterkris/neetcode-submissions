class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # brute force: try all orderings, factorial, doesn't scale

        # dependency graph using adjacency list
        # directed graph
        # adjacency list

        # seen in DFS path vs. fully processed
        # once you explore outgoing edges and confirm no cycle, mark it safe (fully processed)
        # False if see a node currently in our path
        # dfs function (node)
        # revisit a node in curr. path (visiting) -> False
        # node fully processed (visited) -> True
        # explore neighbors using adjacency list
        # if no cycle, mark visited and return True

        # O(V + E) time
        # O(V) space -> adjacency list, visited/visiting sets

        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting: # current path
                return False
            
            if node in visited: # fully checked
                return True
            
            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

            





        