# Maximum path sum II

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#       3
#      7 4
#     2 4 6
#    8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# Use Bellman-Ford to solve this

def determineIndexOffset(i):
  """Determines in what level the of triangle numbers the given index falls"""
  n = 1
  triangleSum = 0
  while i > triangleSum:
    triangleSum = triangleSum + n
    n = n + 1
  return n - 1

def constructGraph(vertices):
  graph = {}
  lenVertices = len(vertices)
  for i in range(1, lenVertices):
    currentV = vertices[ i ]
    currentLabel = 'v' + str(i)
    graph[ currentLabel ] = {}
    indexOffset = determineIndexOffset(i)
    leftChildIndex = i + indexOffset
    rightChildIndex = i + indexOffset + 1
    if leftChildIndex < lenVertices:
      leftChild = vertices[ leftChildIndex ]
      graph[ currentLabel ][ 'v' + str(leftChildIndex) ] = -1 * leftChild
    if rightChildIndex < lenVertices:
      rightChild = vertices[ rightChildIndex ]
      graph[ currentLabel ]['v' + str(rightChildIndex) ] = -1 * rightChild
  return graph

# Implement Bellman-Ford on modified graph
# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
  d = {} # Stands for destination
  p = {} # Stands for predecessor
  for node in graph:
    d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
    p[node] = None
  d[source] = 0 # For the source we know how to reach
  return d, p

def relax(node, neighbour, graph, d, p):
# If the distance between the node and the neighbour is lower than the one I have now
  if d[neighbour] > d[node] + graph[node][neighbour]:
    # Record this lower distance
    d[neighbour]  = d[node] + graph[node][neighbour]
    p[neighbour] = node

def bellman_ford(graph, source):
  d, p = initialize(graph, source)
  for i in range(len(graph)-1): #Run this until is converges
    for u in graph:
      for v in graph[u]: #For each neighbour of u
        relax(u, v, graph, d, p) #Lets relax it

  # Step 3: check for negative-weight cycles
  for u in graph:
    for v in graph[u]:
      assert d[v] <= d[u] + graph[u][v]

  return d, p

def solve(numberPyramid):
  modifiedPyramid = [ "start" ] + map(lambda x: int(x), numberPyramid.split(' '))
  graph = constructGraph(modifiedPyramid)
  paths, predecessors = bellman_ford(graph, 'v1')
  longestPath = modifiedPyramid[ 1 ] + abs(min(paths.values()))
  print("The length of the longest path starting from v1 is %d" % (longestPath))

f = open("triangle.txt", 'r')
s = f.read()
f.close()
s = s.replace("\r\n", ' ').strip()
pyramidOne = s
solve(pyramidOne)
