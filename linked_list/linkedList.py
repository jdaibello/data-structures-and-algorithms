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

    def prepend(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def insert(self, index, value):
        newNode = Node(value)

        if index < 0 or index > self.length:
            return False

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            tempNode = self.head

            for _ in range(index - 1):
                tempNode = tempNode.next

            newNode.next = tempNode.next
            tempNode.next = newNode
            self.length += 1

            return True

    def __str__(self):
        tempNode = self.head
        result = ''

        while tempNode is not None:
            result += f'{tempNode.value}'

            if tempNode.next is not None:
                result += ' -> '

            tempNode = tempNode.next
        return result

newLinkedList = LinkedList()

newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)

print(newLinkedList)
print(newLinkedList.head.value)
print(newLinkedList.tail.value)
print(newLinkedList.length)

newLinkedList.prepend(40)
print(newLinkedList)

newLinkedList.insert(0, 50)
print(newLinkedList)