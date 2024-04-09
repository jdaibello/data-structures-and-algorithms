class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1

    def prepend(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.length += 1

    def traverse(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

    def reverseTraverse(self):
        currentNode = self.tail

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.prev

    def search(self, target):
        currentNode = self.head
        index = 0

        while currentNode:
            if currentNode.value == target:
                return index

            currentNode = currentNode.next
            index += 1

        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            currentNode = self.head

            for _ in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail

            for _ in range(self.length - 1, index, -1):
                currentNode = currentNode.prev

        return currentNode

    def setValue(self, index, value):
        node = self.get(index)

        if node:
            node.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return

        newNode = Node(value)

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return

        tempNode = self.get(index - 1)

        newNode.next = tempNode.next
        newNode.prev = tempNode
        tempNode.next.prev = newNode
        tempNode.next = newNode
        self.length += 1

    def popFirst(self):
        if not self.head:
            return None

        poppedNode = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            poppedNode.next = None

        self.length -= 1

        return poppedNode

    def pop(self):
        if not self.tail:
            return None

        poppedNode = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            poppedNode.prev = None  # Clearing the prev reference

        self.length -= 1

        return poppedNode

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()

        poppedNode = self.get(index)
        poppedNode.prev.next = poppedNode.next
        poppedNode.next.prev = poppedNode.prev
        poppedNode.prev = None
        poppedNode.next = None
        self.length -= 1

        return poppedNode

    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tempNode = self.head
        result = ''

        while tempNode:
            result += str(tempNode.value)

            if tempNode.next:
                result += ' <-> '

            tempNode = tempNode.next

        return result

dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
print(dll)

dll.prepend(50)
dll.prepend(60)
print(dll)

dll.traverse()
dll.reverseTraverse()

print(dll.search(10))
print(dll.get(4).value)

dll.setValue(0, 100)
print(dll)

dll.insert(2, 15)
print(dll)

dll.popFirst()
dll.pop()
print(dll)

dll.remove(2)
print(dll)
