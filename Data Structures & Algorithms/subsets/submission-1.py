class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # declare res array
        # declare subset array

        # we wanna call dfs(0) at the end
        # everytime we reach dfs(len), we add copy to res

        # dfs for backtracking
        # if we have considered i = len(nums) choices in a pass, add copy to res
        # can be mix of not adding anything or adding something

        # we have 2 choices: 
        # include nums[i], call dfs(i + 1)
        # i represents the num of choices made
        # or don't include nums[i], call dfs(i + 1)

        res = []

        subset = []

        def dfs(i):

            if i == len(nums):
               res.append(subset.copy())
               return
            
            subset.append(nums[i])
            dfs(i + 1) # made a choice to add

            subset.pop() # undo adding last val, this is backtracking step
            dfs(i + 1) # made choice not to add

        dfs(0)

        return res


        

