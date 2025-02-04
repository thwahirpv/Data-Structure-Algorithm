class Graph:
    def __init__(self):
        self.vertices = []
        self.graph = {}
    
    def insert(self, vertex):
        if vertex in self.vertices:
            print(vertex, 'already exists!')
            return
        self.vertices.append(vertex)
        self.graph[vertex] = []
        print(vertex, 'added to the graph')
        return
    
    def connect_vertices(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print(vertex1, 'or', vertex2, 'does not exist in the graph!')
            return
        elif vertex2 in self.graph[vertex1]:
            print(vertex1, 'and', vertex2, "are already connected!")
            return
        else:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            print(vertex1, 'and', vertex2, 'are connected')
            return
    
    def delete_vertex(self, vertex):
        if vertex not in self.vertices:
            print(vertex, 'does not exist in the graph!')
            return
        
        self.vertices.remove(vertex)
        connected_vertices = self.graph.pop(vertex)
        for v in connected_vertices:
            self.graph[v].remove(vertex)
        print(vertex, 'deleted!')
        return
    
    def disconnect_vertices(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print(vertex1, 'or', vertex2, 'does not exist in the graph!')
            return
        elif vertex2 not in self.graph[vertex1]:
            print(vertex1, 'and', vertex2, "are not connected!")
            return
        else:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
            print(vertex1, 'and', vertex2, "are disconnected!")
            return
    
    def check_cyclic(self, vertex, visited, parent):
        visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.check_cyclic(neighbor, visited, vertex):
                    return True
            elif parent != neighbor:
                return True
        return False


    def has_cycle(self):
        visited = {v: False for v in self.vertices}

        for vertex in self.vertices:
            if not visited[vertex]:
                if self.check_cyclic(vertex, visited, -1):
                    return True
        return False

    def print_graph(self):
        print(self.vertices)
        for v, connections in self.graph.items():
            print(v, ":", connections)
            print()


grf = Graph()
vertices = ['A', 'B', 'C', 'D', 'E', 'M']
for v in vertices:
    grf.insert(v)

grf.connect_vertices('A', 'B')
grf.connect_vertices('A', 'M')
grf.connect_vertices('B', 'C')
grf.connect_vertices('B', 'D')
grf.connect_vertices('C', 'D')
grf.connect_vertices('C', 'M')
grf.connect_vertices('C', 'E')
grf.connect_vertices('D', 'E')
grf.connect_vertices('M', 'A')

grf.print_graph()

# grf.delete_vertex('D')
# grf.delete_vertex('M')

print(grf.has_cycle())

grf.disconnect_vertices('A', 'D')
grf.disconnect_vertices('B', 'D')

grf.print_graph()

grf.delete_vertex('E')

grf.print_graph()
