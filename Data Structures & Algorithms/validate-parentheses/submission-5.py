class Solution:
    def isValid(self, s: str) -> bool:

        # stack
        # map to store corresponding open/close characters
    
        stack = []
        chars = {')': '(', '}': '{', ']': '['} # map closing to end

        # s = "([{}])"
        # ([{
        # pop
        # ([
        # pop
        # empty
        
        for c in s:
            if c in chars:
               if stack and stack[-1] == chars[c]: # does closing bracket correspond to last opening?
                  stack.pop()
               else:
                    return False 
            else:
                stack.append(c)

        return True if not stack else False 

        
        