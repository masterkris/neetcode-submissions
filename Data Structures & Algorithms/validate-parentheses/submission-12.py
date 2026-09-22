class Solution:
    def isValid(self, s: str) -> bool:

        charMap = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c in charMap:
                if stack and charMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        