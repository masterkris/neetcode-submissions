class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reach = len(nums) - 1  # last index of array

        for i in range(len(nums) - 2, -1, -1): # go from right to left
            if i + nums[i] >= reach: # update "earliest" reach point as we go
                reach = i
        
        return reach == 0
        