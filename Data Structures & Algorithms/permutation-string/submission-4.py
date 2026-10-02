class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # edge case: len(s2) < len(s1), return False

        # hashmap of s1 to store char. frequency

        # hashmap-based sliding window
        # declare l = 0
        # r in range
        # r - l + 1 (len) of window has to be equal to len(s1) at all times
        # if invalid size, move left over
        # take hashmap of current chars. of valid size in s2 and check with s1's hashmap
        # if match, return True
        # if no matches throughout, return False

        if len(s2) < len(s1):
            return False
        
        s1_hashmap = {}
        for c in s1:
            s1_hashmap[c] = 1 + s1_hashmap.get(c, 0)
        
        match = {}
        l = 0

        for r in range(len(s2)):
            match[s2[r]] = 1 + match.get(s2[r], 0)

            while (r - l + 1) > len(s1):
                match[s2[l]] -= 1
                
                if match[s2[l]] == 0: # maintain window size
                    del match[s2[l]] # if we've moved away, delete as its not in current window
            
                l += 1

            if match == s1_hashmap:
                return True
        return False


        