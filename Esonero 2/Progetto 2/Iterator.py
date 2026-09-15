class edgeIter:
    def __init__(self, graph):
        self.index = 0
        self.graph = graph
        self.edges = graph.getEdges()
        self.curr = self.edges[self.index]
        self.max = len(self.edges) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.max:
            raise StopIteration
        self.curr = self.edges[self.index]
        self.index += 1
        return self.curr

