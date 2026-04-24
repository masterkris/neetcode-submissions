class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # sliding window
        # allowed duplicates -> need <= k replacements
        # keep most frequent char, replace rest

        l = 0
        maxf = 0
        res = 0
        freq_map = {} # frequency
        # use set for unique chars

        for r in range(len(s)):
            freq_map[s[r]] = 1 + freq_map.get(s[r],0)
            maxf = max(maxf, freq_map[s[r]])

            while (r - l + 1) - maxf > k: # invalid window
                freq_map[s[l]] -= 1
                l += 1
                # while window is invalid, fix it!
            
            res = max(res, r - l + 1) # if valid, calculate
        
        return res
            
