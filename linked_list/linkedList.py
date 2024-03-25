class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

        return self

newLinkedList = LinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
print(newLinkedList.head.value)
print(newLinkedList.tail.value)