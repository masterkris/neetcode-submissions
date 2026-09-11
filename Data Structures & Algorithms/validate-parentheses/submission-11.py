class Solution:
    def isValid(self, s: str) -> bool:

        charMap = {')' : '(', ']' : '[', '}' : '{'}
        res = []

        for char in s:
            if char in charMap:
                if res and charMap[char] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        return True if not res else False

        