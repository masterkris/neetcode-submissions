class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap and complement approach

        numMap = {} # store index -> val

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numMap:
                return [numMap[complement], i]
            
            numMap[nums[i]] = i


        