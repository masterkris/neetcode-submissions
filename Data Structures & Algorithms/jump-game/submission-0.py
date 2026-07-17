class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reach = len(nums) - 1  # last index of array

        for i in range(len(nums) - 2, -1, -1): # go from left to right
            if i + nums[i] >= reach:
                reach = i
        
        return reach == 0
        