class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        max_n = n

        def dfs(i, n, subset):

            if i == k:
                res.append(subset.copy())
                return
            
            if n > max_n:
                return
            
            subset.append(n)
            dfs(i + 1, n + 1, subset)

            subset.pop()
            dfs(i, n + 1, subset)
        
        dfs(0, 1, [])
        return res
        