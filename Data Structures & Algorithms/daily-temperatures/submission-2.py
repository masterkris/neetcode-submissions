class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for day, val in enumerate(temperatures):
            # enumerate loops through index and value
            while stack and val > temperatures[stack[-1]]: # reached next highest
                prev = stack.pop() # day of last (lower) temp. we "saved" 
                res[prev] = day - prev  # res[prev] as we're starting from prev.

            stack.append(day)
        
        return res
                

        