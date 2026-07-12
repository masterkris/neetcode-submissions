class Solution:
    def countSubstrings(self, s: str) -> int:

        # this is odd, even center question
        # palindrome can either have odd center (1 char) or even center (between 2 chars)
         # palindrome function
         
        def countPalindrome(s, l, r):

    # if l > 0 and r < len(s), and equal (palindrome condition)
            total = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1 # expanding outward from center
                r += 1
            return total

        # now start this function
        
        res = 0

        for i in range(len(s)): # we're doing this for each index in the string btw
            res += countPalindrome(s, i, i) # odd     # abc
            res += countPalindrome(s, i, i + 1) # even  # aaaa
        return res

       

   