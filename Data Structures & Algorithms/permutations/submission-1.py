class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []   

        def backtrack():

            if len(curr) == len(nums): # all curr sets are length of nums
                res.append(curr.copy())
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack()
                    curr.pop() # backtrack

        
        backtrack()
        return res

            
            
        