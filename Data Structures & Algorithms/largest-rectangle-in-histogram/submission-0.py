class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Example 2
        # [0]
        # [0,1]
        # [0, 1, 2]
        # 7 >= 0, pop
        # height = 7, width = 1
        # area = 7
        # repeat, max stays 7
        
        max_area = 0
        stack = []
        n = len(heights)

        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]

            while len(stack) != 0 and heights[stack[-1]] >= curr_height:
                height = heights[stack.pop()] # stack has indices
                if not stack:
                    width = i  # extends to beginning
                else:
                    width = i - stack[-1] - 1 # from first elem. in stack
    
                
                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area