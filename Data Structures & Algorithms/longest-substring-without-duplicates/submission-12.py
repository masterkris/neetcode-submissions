class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        seen = set()
        maxLen = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            maxLen = max(r - l + 1, maxLen)
            seen.add(s[r])
            
        return maxLen
        