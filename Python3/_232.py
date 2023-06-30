# 232: Implement Queue With 2 Stacks
# Push: O(1)
# Peek: O(1) amortized. Move from pushStack into
# popStack needs O(n), but that move readies n
# vals for pop, so O(n) / n == O(1) amortized

class MyQueue:
    def __init__(self):
        self.pushStack = []
        self.popStack  = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)
        
    def pop(self) -> int:
        x = self.peek()
        self.popStack.pop()
        return x

    # Do not push directly into popStack. Rather, only
    # push into popStack by popping from pushStack, for
    # popStack's bottom vals to be pushStack's top/
    # most-recently-pushed vals, as queue needs  
    def peek(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())

        return self.popStack[-1]
        
    # Also check popStack, whose vals came from pushStack
    def empty(self) -> bool:
        return not self.pushStack and not self.popStack
        