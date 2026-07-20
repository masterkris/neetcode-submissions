class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # declare res list

        # define dfs(i, currList, total)
        # curr set (what is currently being built)
        # we wanna call dfs(0, [], 0) at the beginning
        # i -> current index in nums, currList is current list being built
        # total is current sum of numbers in currList
        # we want to reach target

        # Cases:
        # if total == target: add copy of currList to result, return
        # if total > target or i > len(nums), then return. done exploring.
        
        # now we have 2 choices: include nums[i] or skip nums[i]
        # include: add to currentList, call dfs, remove nums[i] to backtrack

        # skip: call dfs(i + 1, currList, total)

        # return res

        res = []

        def dfs(i, currList, total):

            if total == target:
                res.append(currList.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            # take curr. value
            currList.append(nums[i])
            dfs(i, currList, total + nums[i]) # keep i as we can reuse value

            # skip curr. value
            currList.pop() # backtrack
            dfs(i + 1, currList, total)

        dfs(0, [], 0)

        return res

        







        
        