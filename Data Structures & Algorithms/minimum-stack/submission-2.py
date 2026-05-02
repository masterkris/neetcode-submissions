class MinStack:

    # LIFO

    # [2,0]
    # [2]
    # track min. as we go
    # want to know what the min. of all elements is at each step

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)     # [2,0,3]
        val = min(val, self.minStack[-1] if self.minStack else val) # val pushed into minStack is min of entire stack
        self.minStack.append(val)  # [2,0,0]

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # top is for regular stack, min for minStack

    def getMin(self) -> int:
        return self.minStack[-1]
        
