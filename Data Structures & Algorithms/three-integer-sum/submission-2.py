class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort, better handling of duplicates
        # initialize res array
        # for each number in nums, initialize 2 pointers at the next location and the very last location
        # add all of them up, if < 0, move the left pointer right by 1
        # if > 0, we overshot, move the right pointer left by 1
        # ultimately we want == 0
        # if == 0, add to res

        # skip over duplicates (while nums[l] == nums[r])

        nums.sort()

        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue # skip
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                
                elif total > 0:
                    r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res



        