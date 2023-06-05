class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def vertex(self):
        print("\nSeluruh Node = ", end="")
        for key in self._data.keys():
            print(key, end=" ")
        print()

    def edge(self):
        print("Seluruh Edge = ", end="")
        visited = set()
        for key in self._data.keys():
            for neighbor in self._data[key]:
                if (key, neighbor) not in visited and (neighbor, key) not in visited:
                    visited.add((key, neighbor))
                    visited.add((neighbor, key))
                    print(f"({key}, {neighbor})", end=" ")
        print()

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)

    def bfs(self, node):
        visited = set()
        queue = []
        queue.append(node)
        visited.add(node)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            neighbors = self._data[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        print("\n")


graph = Graph()

# Menambahkan vertex
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

# Menambahkan edge
graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('d', 'e')
graph.addEdge('e', 'f')

# Menampilkan seluruh vertex
graph.vertex()

# Menampilkan seluruh edge
graph.edge()

# Melakukan traversal BFS 
graph.bfs("a")
