from AdjacencyListGraph import graph


def DFS_caller(adjL):
   visited = list()
   start = list(adjL.keys())[0]
   print("start: ", start)
   DFS(start, visited, adjL)
   print(visited)


def DFS(curr_node, visited, adjL):
   visited.append(curr_node)
   for point in adjL[curr_node]:
      if point not in visited:
         DFS(point, visited, adjL)

g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(4, 2)
g.addEdge(3, 0)
g.addEdge(1, 3)

DFS_caller(g.adjList)
