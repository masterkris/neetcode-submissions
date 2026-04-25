class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1  # skip over invalid characters
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): # now we have two comparable chars
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c): #  all valid chars
            return (ord('A') <= ord(c) <= ord('Z') 
            or ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')) # unicode point