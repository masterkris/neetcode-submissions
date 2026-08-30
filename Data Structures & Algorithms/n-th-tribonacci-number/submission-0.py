class Solution:
    def tribonacci(self, n: int) -> int:

        t = [0, 1, 1]

        if n < 3:
            return t[n]
        
        for i in range(3, n + 1):
            t[i % 3] = t[0] + t[1] + t[2]
            # i = 3 -> t[0] = 2
            # i = 4 -> t[1] = 4
            # i = 5 -> t[2] = 7
        
        return t[n % 3]
        