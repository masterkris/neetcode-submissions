class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop() + stack.pop()))
            elif token == "-":
                stack.append(int((-1) * (stack.pop() - stack.pop())))
            elif token == "*":
                stack.append(int((stack.pop() * stack.pop())))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
            else:
                # default case
                stack.append(int(token))
        
        return stack[-1]

