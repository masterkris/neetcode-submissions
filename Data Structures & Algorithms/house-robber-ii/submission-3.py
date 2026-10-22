class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge case: if nums is only len 1, return that element

        if len(nums) == 1:
            return nums[0]

        def robHelper(nums):
          # rob2, rob1, n, n + 1, n + 2
          rob2 = 0
          rob1 = 0

          for n in nums:
            curr = max(rob2 + n, rob1)

            rob2 = rob1
            rob1 = curr
           
          return curr
        
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))

         
        
        