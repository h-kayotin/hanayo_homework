"""
92_最小栈 - 

Author: hanayo
Date： 2024/6/20
"""


class MinStack:
    """巧妙之处在于用一个元组，(当前值，当前最小值)"""

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self):
        pop_val = self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]