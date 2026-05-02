class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # traverse tokens and add to stack
        # when sign seen +, *, -, /, pop previous and do operations as needed
        # O(n) time
        # O(1) space

        stack = []

        for token in tokens:
            if token == "+":
                sum = stack.pop() + stack.pop()
                stack.append(int(sum))
            elif token == "-":
                diff = (stack.pop() - stack.pop()) * (-1)
                stack.append(int(diff))
            elif token == "*":
                prod = (stack.pop() * stack.pop())
                stack.append(int(prod))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                quo = int(b/a) 
                stack.append(quo)
            else:
                stack.append(int(token))
        
        return stack[-1]
        