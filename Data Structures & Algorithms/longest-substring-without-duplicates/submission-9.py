class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # as long as new char, count and expand window
        # when previous char that we've seen shows up again, then restart count
        # expand window -> add to seen
        # shrink window -> remove from seen
        # return max substring size

        l = 0
        longest = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest


        