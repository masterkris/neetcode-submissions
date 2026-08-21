class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, currList, total):

            if total == target:
                res.append(currList.copy())
                return
            
            if total > target or i == len(nums):
                return
            
            # either take or skip curr. value
            
            currList.append(nums[i])
            # i is current index in nums.
            dfs(i, currList, total + nums[i])

            currList.pop()
            dfs(i + 1, currList, total)
        
        dfs(0, [], 0)

        return res
            

        