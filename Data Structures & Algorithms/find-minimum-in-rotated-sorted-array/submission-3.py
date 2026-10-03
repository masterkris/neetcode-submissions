class Solution:
    def findMin(self, nums: List[int]) -> int:

        # l = 0, r = len(nums) - 1
        # find middle index and element
        # comparing middle element to the r value
        # if middle element > right value
        # binary search from the next elem. to end (as min is to right)
        # if middle element < right value
        # set the current element as the right value (as min is at mid to left)

        # O(log n) time, O(1) space

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2 # truncating operator

            if nums[m] > nums[r]:
                l = m + 1
            
            elif nums[m] < nums[r]:
                r = m
            
        return nums[l]
        
        