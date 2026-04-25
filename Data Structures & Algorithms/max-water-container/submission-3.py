class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # l, r pointers, iterate
        # if heights[l] < heights[r], move r pointer. otherwise move l pointer.
        # calculate area -> (min(heights[r] - heights[l]) * (r-l))
        
        l, r = 0, len(heights) - 1
        maxWater = 0

        while (l < r):
            maxWater = max(maxWater, min(heights[r], heights[l]) * (r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater