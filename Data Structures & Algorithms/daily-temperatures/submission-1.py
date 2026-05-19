class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for day, val in enumerate(temperatures): # keep track of index and value
            while len(stack) != 0 and val > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = day - prev # store days to next highest (index)
            
            stack.append(day) 

        return res

        # 38 -> 40
        # stack: [1,2,3]
        # pop until prev = 1
        # res[1] = 5 - 1 = 4
        