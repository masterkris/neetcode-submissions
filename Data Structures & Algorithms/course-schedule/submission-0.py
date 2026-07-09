class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # first hashmap for course to prereqs

        preMap = {}

        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        visiting = set() # store courses along DFS path

        # good to detect duplicates

        def dfs(crs):
            if crs in visiting: # cycle
                return False
            
            visiting.add(crs) # add to set

            for pre in preMap[crs]: # check every prereq of curr. course

            # run DFS on prereq, if prereq can't be completed, curr. course can't be completed
                if not dfs(pre):
                    return False
                
            visiting.remove(crs) # explored course, removed from DFS path

            preMap[crs] = [] # clear prereq. list
            return True
        
        for c in range(numCourses):
            if not dfs(c): # DFS from every course to ensure we check entire graph for cycles
                return False
        
        return True



        