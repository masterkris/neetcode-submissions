class Solution:
    def romanToInt(self, s: str) -> int:
        
        rtoi_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C" : 100, "D": 500, "M": 1000}

        total = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s) and rtoi_map[s[i]] < rtoi_map[s[i+1]]:
                total += (rtoi_map[s[i+1]] - rtoi_map[s[i]])
                i += 2
            else:
                total += rtoi_map[s[i]]
                i += 1
        
        return total
