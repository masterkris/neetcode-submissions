class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # hashmap-based window --> counts/frequencies like this problem
        # right expands -> add element, update
        # if window invalid -> move left until valid
        # update answer

        l = 0
        longest = 0 
        maxFreq = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]]) # freq. of latest / current char. 

            # window size - most freq. char = replacements needed --> XYY
            # invalid window, adjust to make valid
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest

        