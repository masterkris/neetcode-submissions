class Solution:
    def trap(self, height: List[int]) -> int:

        # similar two pointer problem to container with most water
        # except constraint of walls in the way
        # l, r
        # example in pic --> 3, 1, 0, 1, 3 (max is 7) - 3 x 3 - 1 - 1 = 7
        # calculate area between two points and subtract vals in between
        # update maximum
        # O(n) time -> traverse fully
       
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        maxWater = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                maxWater += (leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                maxWater += (rightMax - height[r])
        
        return maxWater


        
        