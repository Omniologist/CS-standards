from AdjacencyListGraph import graph

def BFS(adjList):
    visited = list()
    queue = list()
    queue.append(list(adjList.keys())[0])
    while queue:
        queue.extend(list(set(adjList[queue[0]]) - set(visited) - set(queue)))
        visited.append(queue[0])
        print(queue.pop(0))
    print(visited)

g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 6)
g.addEdge(5, 7)
g.addEdge(6, 8)

g.printAdjList()

BFS(g.adjList)