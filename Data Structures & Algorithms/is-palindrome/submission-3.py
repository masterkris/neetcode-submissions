class Solution:
    def isPalindrome(self, s: str) -> bool:

        # l and r pointers
        # from beginning and end
        # if not same at any point, return False

        l = 0
        r = len(s) - 1

        while l < r:
            # skip over invalid chars
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
                
            l += 1
            r -= 1

        return True
    
    def alphaNum(self, c): # all valid chars

        return (ord('A') <= ord(c) <= ord('Z')
        or ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))
    

        