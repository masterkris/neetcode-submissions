class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # hashmap-based sliding window
        # declare l = 0, longest = 0, maxFreq = 0
        # declare hashmap
        # for loop -> r in range
        # add to hashmap, update longest
        # num. replacements = (r - l + 1) - maxFreq --> invalid condition, so remove l while invalid
        # have to make sure <= k
        # if > k, shrink window
        # update longest

        l = 0
        longest = 0
        maxFreq = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(r - l + 1, longest)
        
        return longest



       


        



        