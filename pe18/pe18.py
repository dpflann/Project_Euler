# Maximum path sum I

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#       3
#      7 4
#     2 4 6
#    8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom of the triangle below:
#
#                           75
#                         95 64
#                       17 47 82
#                     18 35 87 10
#                   20 04 82 47 65
#                 19 01 23 75 03 34
#                88 02 77 73 07 63 67
#              99 65 04 28 06 16 70 92
#             41 41 26 56 83 40 80 70 33
#           41 48 72 33 47 32 37 16 94 29
#         53 71 44 65 25 43 91 52 97 51 14
#       70 11 33 28 77 73 17 78 39 68 17 57
#      91 71 52 38 17 14 91 43 58 50 27 29 48
#    63 66 04 68 89 53 67 30 73 16 69 87 40 31
#  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing 
# one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# Use Bellman-Ford to solve this

vertices = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
vertices = vertices.split(' ')
vertices = ['start'] + vertices

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


pyramidOne = """3 7 4 2 4 6 8 5 9 3"""
solve(pyramidOne)

pyramidTwo = """75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

solve(pyramidTwo)
