class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # backtracking

        # aab can be broken down into aa, b OR a, a, b
        # if possible solution, i = len(s)

        res = []

        part = [] # curr. partition

        def dfs(i): # i = index of current char
            # base case
            if i >= len(s):
                res.append(part.copy())
                return
            
            # generate every possible pali. substring from i to j
            for j in range(i, len(s)):
                if self.isPali(s, i, j): # start at index i, end at index j
                    part.append(s[i: j + 1])
                    dfs(j + 1) # start from next char.
                    # after we've recursed and found all partitions, backtrack
                    part.pop()
            
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            

        