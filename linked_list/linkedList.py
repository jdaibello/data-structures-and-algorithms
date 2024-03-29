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

    def traverse(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0

        while current:
            if current.value == target:
                return index

            current = current.next
            index += 1

        return -1

    def get(self, index):
        if index == -1:
            return self.tail

        if index < -1 or index >= self.length:
            return None

        current = self.head

        for _ in range(index):
            current = current.next

        return current

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

        self.length -= 1

        return poppedNode

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            return self.popFirst()

        else:
            poppedNode = self.tail
            temp = self.head

            while temp.next != self.tail:
                temp = temp.next

            temp.next = None
            self.tail = temp
            self.length -= 1

            return poppedNode

    def remove(self, index):
        if self.head is None or index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.popFirst()

        if index == self.length - 1 or index == -1:
            return self.pop()

        prevNode = self.get(index - 1)
        poddedNode = prevNode.next
        prevNode.next = poddedNode.next
        poddedNode.next = None
        self.length -= 1

        return poddedNode.value

    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0

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
newLinkedList.traverse()
print(newLinkedList.search(30))
print(newLinkedList.get(2).value)
print(newLinkedList)
print(newLinkedList.setValue(2, 50))
print(newLinkedList)
print(newLinkedList.popFirst())
print(newLinkedList)
print(newLinkedList.pop())
print(newLinkedList)
print(newLinkedList.remove(1))
print(newLinkedList)
print(newLinkedList.deleteAll())