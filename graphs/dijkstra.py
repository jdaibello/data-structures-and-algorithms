import heapq

class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.minDistance = float('inf')

    def addEdge(self, weight, destinationVertex):
        edge = Edge(weight, self, destinationVertex)
        self.neighbors.append(edge)

    def __lt__(self, otherNode):
        return self.minDistance < otherNode.minDistance

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, startVertex):
        startVertex.minDistance = 0
        heapq.heappush(self.heap, startVertex)

        while self.heap:
            # Pop element with the lowest distance
            actualVertex = heapq.heappop(self.heap)

            if actualVertex.visited:
                continue

            # Consider the neighbors
            for edge in actualVertex.neighbors:
                start = edge.startVertex
                target = edge.targetVertex
                newDistance = start.minDistance + edge.weight

                if newDistance < target.minDistance:
                    target.minDistance = newDistance
                    target.predecessor = start

                    # Update the heap
                    heapq.heappush(self.heap, target)

            actualVertex.visited = True

    def getShortestPath(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.minDistance}")
        actualVertex = vertex

        while actualVertex is not None:
            print(f"{actualVertex.name}", end=' ')
            actualVertex = actualVertex.predecessor

# Step 1 - Create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2 - Create edges
nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(5, nodeH)
nodeC.addEdge(21, nodeG)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(4, nodeE)
nodeF.addEdge(12, nodeG)

nodeH.addEdge(2, nodeF)
nodeH.addEdge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeG)