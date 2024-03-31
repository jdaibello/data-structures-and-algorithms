class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue

    def delete(self):
        self.linkedList.head = None

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.isEmpty())
print(customStack)

customStack.pop()
print(customStack)

print(customStack.peek())