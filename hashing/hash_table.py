class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return

        prev = None

        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next

        prev.next = HashNode(key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        if prev is None:
            self.buckets[index] = node.next
        else:
            prev.next = node.next

        self.size -= 1
        return node.value

hashTable = HashTable()

hashTable.insert("one", 1)
hashTable.insert("two", 2)
print(hashTable.get("one")) # 1

hashTable.remove("one")
print(hashTable.get("one")) # None