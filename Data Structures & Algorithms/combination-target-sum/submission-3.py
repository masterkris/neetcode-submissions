class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # res array
        # subset array

        # dfs function (i, subset, remaining sum)
        # base case: if target value reached, append copy subset
        # if remaining goes negative, we stop
        # if remaining is zero, append copy subset to res

        # take or not take value
        # add same value to subset

        # skip and move to next
        # time complexity -> exponential in depth
        # space complexity -> depth for call stack + output

        res = []
        subset = []

        def dfs(i, subset, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            
            if remaining < 0:
                return
            
            if i == len(nums):
                return
            
            # same choice
            subset.append(nums[i])
            dfs(i, subset, remaining - nums[i])

            # 
            subset.pop()
            dfs(i + 1, subset, remaining)
        
        dfs(0, [], target)
        return res

