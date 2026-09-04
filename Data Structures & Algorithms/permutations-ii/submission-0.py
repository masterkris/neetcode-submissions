class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        def dfs(curr):

            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    curr.append(n)
                    count[n] -= 1
                    dfs(curr) # recurse
                    curr.pop() # backtrack
                    count[n] += 1 # re-add after backtrack
        
        dfs([])
        return res

            
            

       
            

        