__author__ = 'robbie'

class mystack(list):

    def __init__(self):
        self = []

    def push(self, c):
        self.append(c)

    def peek(self):
        i = len(self) - 1
        return self[i]

    def isEmpty(self):
       return len(self) == 0


stack = mystack()
stack.append(3)
stack.append(5)
stack.pop()

print(stack.peek())
print(stack)
