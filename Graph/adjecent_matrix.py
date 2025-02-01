class Graph:
    def __init__(self):
        self.vertices = []
        self.graph = []
        self.vertix_count = 0
    
    def add_vertix(self, vertix):
        if vertix in self.graph:
            print(vertix, 'already exist!')
            return
        self.vertices.append(vertix)
        self.vertix_count += 1
        for row in self.graph:
            row.append(0)
        temp = [0] * self.vertix_count
        self.graph.append(temp) 
    
    def add_edge(self, vertixOne, vertixTwo):
        if vertixOne not in self.vertices:
            print(vertixOne, 'not present in Graph')
            return 
        elif vertixTwo not in self.vertices:
            print(vertixTwo, 'not present in graph')
            return 
        else:
            v1 = self.vertices.index(vertixOne)
            v2 = self.vertices.index(vertixTwo)
            self.graph[v1][v2] += 1
            self.graph[v2][v1] += 1
            print('Edge added between', vertixOne, 'and', vertixTwo)
            return 
    
    def delete_vertix(self, vertix):
        if vertix not in self.vertices:
            print(vertix, 'not exits!')
            return 
        index = self.vertices.index(vertix)
        self.vertices.pop(index)
        self.vertix_count -= 1
        self.graph.pop(index)
        for row in self.graph:
            row.pop(index)
        print(vertix, 'deleted!')
        return

    def delete_edge(self, vertixOne, vertixTwo):
        if vertixOne not in self.vertices:
            print(vertixOne, 'not exits!')
            return 
        elif vertixTwo not in self.vertices:
            print(vertixTwo, 'not exits!')
            return 
        else:
            v1 = self.vertices.index(vertixOne)
            v2 = self.vertices.index(vertixTwo)
            self.graph[v1][v2] = 0 if self.graph[v1][v2]-1 < 0 else self.graph[v1][v2] - 1
            self.graph[v2][v1] = 0 if self.graph[v2][v1]-1 < 0 else self.graph[v2][v1] - 1
            print('Edge between', vertixOne, 'and', vertixTwo, 'deleted!')
            return
    
    def printGraph(self):
        if len(self.graph) is 0:
            print('Graph is empty!')
            return 
        for row in self.graph:
            print()
            print(row)
        return
        
        


grf = Graph()
grf.add_vertix('A')
grf.add_vertix('B')
grf.add_vertix('C')
grf.add_vertix('D')

grf.add_edge('A', 'B')
grf.add_edge('C','A')
grf.add_edge('C','D')
grf.add_edge('A', 'B')
grf.delete_vertix('A')
grf.printGraph()

grf.delete_edge('A', 'B')


grf.printGraph()