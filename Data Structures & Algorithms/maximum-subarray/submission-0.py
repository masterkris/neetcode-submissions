class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        # track max subarray sum and curr sum 
        # iterate through nums array
        # if sum ever becomes -ve
        # then reset curr sum to 0 (Kadane's)
        # increment curr sum
        # max subarray sum update to max of maxSub and currSum
        # return maxSub

        maxSubSum, currSum = nums[0], 0

        for num in nums:
            if currSum < 0: # Kadane's algo, -ve at any point won't be max
               currSum = 0
            
            currSum += num
            maxSubSum = max(maxSubSum, currSum)

        return maxSubSum





        
        