class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for day, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = day - prev
        
            stack.append(day)
        
        return res
        