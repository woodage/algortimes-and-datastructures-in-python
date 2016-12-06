__author__ = 'robbie'

class mystack:

    def __init__(self):
        self.stack = []

    def push(self, c):
        self.stack.append(c)

    def pop(self):
        self.stack.pop()

    def peek(self):
        i = len(self.stack) - 1
        return self.stack[i]

    def isEmpty(self):
        if not self.stack:
            return True

        return False
