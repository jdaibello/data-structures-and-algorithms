class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CircularSinglyLinkedList:
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
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode  # Pointing the tail's next to the new head
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:  # Check for out of range
            raise Exception("Index out of range")

        newNode = Node(value)

        if index == 0:
            if self.length == 0:  # if list is empty
                self.head = newNode
                self.tail = newNode
                newNode.next = newNode
            else:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode  # Update tail's next for circularity
        elif index == self.length:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
        else:
            temp_node = self.head

            for _ in range(index-1):
                temp_node = temp_node.next

            newNode.next = temp_node.next
            temp_node.next = newNode

        self.length += 1

    def traverse(self):
        if not self.head:  # If the list is empty
            return

        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

            if current == self.head:  # Stop condition for circular list
                break

    def search(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True

            current = current.next

            if current == self.head:  # Stop condition for circular list
                break

        return False

    def search(self, target):
        current = self.head
        index = 0

        while current is not None:
            if current.value == target:
                return index

            current = current.next
            index += 1

        return -1

    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
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
            self.tail.next = self.head  # Update the tail's next pointer to point to the new head
            poppedNode.next = None

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
            temp = self.head

            while temp.next != self.tail:  # Traverse until the second last node
                temp = temp.next

            temp.next = self.head  # Pointing the second last node's next to the head
            self.tail = temp  # Updating the tail to be the second last node

        poppedNode.next = None
        self.length -= 1

        return poppedNode

    def remove(self, index):
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == -1 or index == self.length-1:
            return self.pop()

        previousNode = self.get(index - 1)
        poppedNode = previousNode.next
        previousNode.next = poppedNode.next
        poppedNode.next = None
        self.length -= 1

        return poppedNode

    def deleteAll(self):
        if self.length == 0:
            return  # If the list is empty, just return

        self.tail.next = None  # Breaking the circular link
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:  # Stop condition for circular list
                break

            result += ' -> '

        return result

linkedList = CircularSinglyLinkedList()
print(linkedList)

linkedList.append(10)
linkedList.append(20)
print(linkedList)

linkedList.prepend(30)
print(linkedList)

linkedList.prepend(40)
print(linkedList)

linkedList.insert(0, 20)
linkedList.insert(1, 30)
linkedList.insert(2, 40)
print(linkedList)

linkedList.traverse()

print(linkedList.get(-1))
print(linkedList.setValue(-1, 100))
print(linkedList)

print(linkedList.popFirst())

linkedList.pop()
print(linkedList)

print(linkedList.remove(1))
print(linkedList)
