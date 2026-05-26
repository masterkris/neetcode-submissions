class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        index = 0

        while (l <= r):
            m = (l + r) // 2

            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                # [5,6..] or #[..6,1,2]
                if nums[m] < target or nums[l] > target: # nums[m] = 5, target = 6 (for example)
                    l = m + 1 
                else:
                    r = m - 1 

            else:
                if nums[m] > target or target > nums[r]: # nums[m] = 5, target = 1
                    r = m - 1 
                else:
                    l = m + 1
        
        return -1