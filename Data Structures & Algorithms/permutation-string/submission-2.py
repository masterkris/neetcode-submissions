class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # length of s1 has to be less than s2, check edge case
        # use hashmap sliding window
        # target hashmap
        # current hashmap
        # check if they match at any point -> return true

        if len(s1) > len(s2):
            return False
        

        # looking at freq. of chars.

        target = {}
        current = {}

        for c in s1:
            target[c] = 1 + target.get(c, 0)
        
        # sliding window starts here

        l = 0

        for r in range(len(s2)):
            current[s2[r]] = 1 + current.get(s2[r], 0)

            if r - l + 1 > len(s1):
                current[s2[l]] -= 1 # match to size of s1
            
                if current[s2[l]] == 0:
                    del current[s2[l]]
                
                l += 1
                
            if current == target:
                return True
        
        return False


        