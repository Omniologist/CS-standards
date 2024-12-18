class graph:
    def __init__(self):
        self.adjList = dict()
    def addEdge(self, a, b):
        if a not in self.adjList.keys():
            self.adjList.update({a:list()})
        if b not in self.adjList.keys():
            self.adjList.update({b:list()})
        self.adjList[a].append(b)
        
    def printAdjList(self):
        for key, nodeList in self.adjList.items():
            print(str(key)+", ", end="")
            for item in nodeList:
                print(str(item)+", ", end="")
            print("\n")