class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, subset, total):

            if total == 0:
                res.append(subset.copy())
                return
            
            if total < 0 or i == len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, total - candidates[i])

            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1 # skip duplicates

            dfs(i + 1, subset, total)
        
        dfs(0, [], target)
        return res
            

        