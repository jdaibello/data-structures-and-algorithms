class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def isEmpty(self):
        if self.list == [] or self.list == None:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'The element has been successfully added to the stack'

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

customStack = Stack(4)

print(customStack.isEmpty())
print(customStack.isFull())

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print(customStack.peek())