class Solution:
    def rob(self, nums: List[int]) -> int:

        # variation of House Robber I
        # but constraint is circular
        # so could exclude first or exclude last
        # so we need to account for starting from 1 vs. last
        
        # edge case
        if len(nums) == 1:
            return nums[0]

        def robHelper(nums):

            rob1, rob2 = 0, 0

            for n in nums:
                curr = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = curr
            return rob2

        return max(robHelper(nums[1:]), robHelper(nums[:-1]))



        