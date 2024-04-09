class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            self.tail.next = newNode
            self.head.prev = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail = newNode

        self.length += 1

    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            self.tail.next = newNode
            self.head.prev = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def traverse(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

            if currentNode == self.head:
                break

    def reverseTraverse(self):
        currentNode = self.tail

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.prev

            if currentNode == self.tail:
                break

    def search(self, target):
        current = self.head

        while current:
            if current.value == target:
                return True

            current = current.next

            if current == self.head:
                break

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return

        newNode = Node(value)
        tempNode = self.get(index - 1)

        newNode.next = tempNode.next
        newNode.prev = tempNode
        tempNode.next.prev = newNode
        tempNode.next = newNode

        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        currentNode = None

        if index < self.length // 2:
            currentNode = self.head

            for i in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail

            for i in range(self.length - 1, index, -1):
                currentNode = currentNode.prev

        return currentNode

    def setValue(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def popFirst(self):
        if self.length == 0:
            return None

        poppedNode = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            poppedNode.next = None
            poppedNode.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head

        self.length -= 1

        return poppedNode

    def pop(self):
        if self.length == 0:
            return None

        poppedNode = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            poppedNode.prev = None
            poppedNode.next = None
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -= 1

        return poppedNode

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()

        poppedNode = self.get(index)
        poppedNode.prev.next = poppedNode.next
        poppedNode.next.prev = poppedNode.prev
        self.length -= 1

        return poppedNode

    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        currentNode = self.head

        while currentNode:
            result += str(currentNode.value)
            currentNode = currentNode.next

            if currentNode == self.head: break
            result += ' <-> '

        return result

cdll = CircularDoublyLinkedList()

cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
print(cdll)

cdll.prepend(90)
print(cdll)

cdll.traverse()
cdll.reverseTraverse()

print(cdll.search(10))
print(cdll.get(0).value)

print(cdll.setValue(2, 50))
print(cdll)

cdll.insert(1, 60)
print(cdll)

cdll.popFirst()
cdll.pop()
print(cdll)

cdll.remove(1)
print(cdll)
