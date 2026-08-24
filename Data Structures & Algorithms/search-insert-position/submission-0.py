class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # declare l and r
        # find mid
        # if nums[mid] < target, l = mid + 1
        # if nums[mid] > target, r = mid - 1
        # if nums[mid] == target, return mid
        # else return l, as l is the index we have to insert into

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            
            if nums[mid] > target:
                r = mid - 1
            
            if nums[mid] == target:
                return mid
        
        return l
        