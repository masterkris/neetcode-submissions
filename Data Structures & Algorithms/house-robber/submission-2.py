class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # rob1 rob2 n rob rob

        rob1 = 0 # until n - 2
        rob2 = 0 # until n - 1

        for n in nums:
            curr = max(rob1 + n, rob2)

            rob1 = rob2
            rob2 = curr
        
        return curr