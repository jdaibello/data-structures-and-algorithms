import queueLinkedList as queue

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTreeNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTreeNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "The node has been successfully inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def minValueNode(bstNode):
    current = bstNode

    while (current.leftChild is not None):
        current = current.leftChild

    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode

    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The Binary Search Tree has been successfully deleted"

newBinarySearchTree = BinarySearchTreeNode(None)

insertNode(newBinarySearchTree, 70)
insertNode(newBinarySearchTree, 50)
insertNode(newBinarySearchTree, 90)
insertNode(newBinarySearchTree, 30)
insertNode(newBinarySearchTree, 60)
insertNode(newBinarySearchTree, 80)
insertNode(newBinarySearchTree, 100)
insertNode(newBinarySearchTree, 20)
insertNode(newBinarySearchTree, 40)

preOrderTraversal(newBinarySearchTree)
print('***************')

inOrderTraversal(newBinarySearchTree)
print('***************')

postOrderTraversal(newBinarySearchTree)
print('***************')

levelOrderTraversal(newBinarySearchTree)
print('***************')

searchNode(newBinarySearchTree, 80)
print('***************')

deleteNode(newBinarySearchTree, 20)
levelOrderTraversal(newBinarySearchTree)
