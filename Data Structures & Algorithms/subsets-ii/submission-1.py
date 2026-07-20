class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # can choose to add or not to add
        # i is num. of choices here

        res = []
        nums.sort()

        def dfs(i, subset):

            if i == len(nums):
                res.append(subset.copy())
                return
            
            # take case
            subset.append(nums[i])
            dfs(i + 1, subset)


            subset.pop()

            # check for duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # skip case
            dfs(i + 1, subset)
        
        dfs(0, [])
        
        return res

        