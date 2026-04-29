class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # have, need --> should be equal
        # curr_window, T
        # check if T hashmap is equal to what we have in window
        # remove left character once found, and keep going to find min.
        # remove irrelevant left chars (not in t)
        # keep going until invalid

        # edge case
        if t == "":
            return ""
        
        curr = {}
        t_map = {}

        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)
        
        have, need = 0, len(t_map)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            curr[s[r]] = 1 + curr.get(s[r],0)

            if s[r] in t_map:
                if curr[s[r]] == t_map[s[r]]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
            
                # shrink from left
                curr[s[l]] -= 1

                if s[l] in t_map and curr[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] 

        