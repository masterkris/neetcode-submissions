class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numCount = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in numCount:
                return [numCount[complement], i]
            
            numCount[nums[i]] = i

        