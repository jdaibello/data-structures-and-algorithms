class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList.keys():
            self.adjacencyList[vertex] = []
            return True
        return False

    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex, ":", self.adjacencyList[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList.keys() and vertex2 in self.adjacencyList.keys():
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList.keys() and vertex2 in self.adjacencyList.keys():
            try:
                self.adjacencyList[vertex1].remove(vertex2)
                self.adjacencyList[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjacencyList.keys():
            for other_vertex in self.adjacencyList[vertex]:
                self.adjacencyList[other_vertex].remove(vertex)
            del self.adjacencyList[vertex]
            return True
        return False

my_graph = Graph()

my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")

my_graph.addEdge("A", "B")
my_graph.addEdge("A", "C")
my_graph.addEdge("A", "D")
my_graph.addEdge("B", "C")
my_graph.addEdge("C", "D")

my_graph.printGraph()

my_graph.removeVertex("A")

print("After remove...")
my_graph.printGraph()