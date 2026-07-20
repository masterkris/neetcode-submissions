class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # not sorted, have to sort
        # and dfs(i + 1 ...) on both calls since 
        # otherwise, similar to combination sum I

        res = []

        candidates.sort()

        def dfs(i, currList, total):

            if total == target:
                res.append(currList.copy())
                return

            if total > target or i == len(candidates):
                return
            
            currList.append(candidates[i])
            dfs(i + 1, currList, total + candidates[i]) # take case

            currList.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, currList, total) # skip case

        
        dfs(0, [], 0)

        return res
        