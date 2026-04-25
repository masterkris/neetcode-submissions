class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1Count, s2Count hashmaps (a -> z, 26 chars)
        # matches tells us match between 2 strings for each window
        # 26 matches = exact match, all chars match = stop algorithm and return True
        # window size in s2 is size of s1 
        # we can just do hashmap approach
        # for each iteration of window, compare hashmaps

        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        for c in s1:
            target[c] = 1 + target.get(c, 0)

        # sliding window
        l = 0

        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0) # hashmap

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1  # keep window size length of s1

                if window[s2[l]] == 0: # key = 0
                    del window[s2[l]]
               
                l += 1
            
            if window == target: # if equal, return True immediately
                return True
            
        return False




        
        