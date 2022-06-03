import collections


class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

example_graph = Graph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def search(graph, start):
    f = Queue()
    f.put(start)
    visited = {}
    visited[start] = True

    while not f.empty():
        current = f.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                f.put(next)
                visited[next] = True


search(example_graph, 'A')



