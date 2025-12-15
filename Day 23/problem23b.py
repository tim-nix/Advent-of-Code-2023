import time

def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines


# From the trails map, extract all locations that are
# intersections; that is, have either 3 or 4 non-tree
# neighbors.  Add the start and stop locations to the
# nodes collection.
def buildNodes(trails, start, stop):
   deltas = [ (0, -1), (0, 1), (-1, 0), (1, 0) ]
   
   adjacencies = dict()
   # Add the start node to the node collection and adjacencies.
   nodes = [ start ]
   adjacencies[start] = [ (start[0] + 1, start[1]) ]
   # Iterate through each location on the trail map.
   for x in range(len(trails)):
      for y in range(len(trails[x])):
         # If the current location is not a tree, then
         # get each of its non-tree neighbors (n, s, e, w).
         if trails[x][y] != '#':
            adjacents = []
            for delta_x, delta_y in deltas:
               if ((0 <= (x + delta_x) < len(trails)) and (0 <= (y + delta_y) < len(trails[x]))):
                  if trails[x + delta_x][y + delta_y] != '#':
                     adjacents.append((x + delta_x, y + delta_y))

            # If the node has more than two neighbors, then
            # add it to the collection.  Also, add the
            # neighbors to the adjacency dictionary.
            if len(adjacents) > 2:
               nodes.append((x, y))
               adjacencies[(x, y)] = tuple(adjacents)

   # Also add the stop node to the collection and adjacencies.
   nodes.append(stop)
   adjacencies[stop] = [ (stop[0] - 1, stop[1]) ]
   
   return (nodes, adjacencies)


# Build a list of paths between the nodes; that is,
# determine if a path exists between two nodes and
# determine the associated distance.  If a path
# exists, add it to the list of shortcuts.
def buildPaths(trails, nodes, adjacencies):
   shortcuts = []
   deltas = [ (0, -1), (0, 1), (-1, 0), (1, 0) ]
   finish = set(nodes)
   # Look through all nodes.
   while len(nodes) > 0:
      start = nodes.pop(0)
      visited = set()
      visited.add(start)
      # Follow a path from each adjacent neighbor to
      # another node.  Add the two endpoints and the
      # distance to shortcuts.
      for neighbor in adjacencies[start]:
         #print('neighbor = ' + str(neighbor))
         distance = 1
         current = neighbor
         # Keep following the path as long as it is
         # not at an intersection.
         while (current not in finish):
            x, y = current
            visited.add((x, y))
            distance += 1
            toVisit = []
            for delta_x, delta_y in deltas:
               if ((0 <= (x + delta_x) < len(trails)) and
                   (0 <= (y + delta_y) < len(trails[x]))):
                  if (((x + delta_x, y + delta_y) not in visited) and
                      (trails[x + delta_x][y + delta_y] != '#')):
                     toVisit.append((x + delta_x, y + delta_y))

            # Update the location
            current = toVisit[0]

         # Once the next node is reached, add the
         # shortcut to the collection.
         shortcuts.append((start, current, distance))

   return shortcuts       


# Build an adjacency matrix for the graph. The graph
# is weighted, non-directed. The weights are the values
# found in shortcuts. The function also returns the
# index values for the start and step locations.
def buildGraph(shortcuts, adjacencies, start, stop):
   # The adjacencies dictionary keys provide the
   # mapping from (x, y) location to the index into
   # the adjacency matrix.
   nodes = list(adjacencies.keys())

   # Create an empty adjacency matrix of correct size.
   graph = [ [ 0 for y in range(len(nodes)) ] for x in range(len(nodes)) ]

   # Map each shortcut to the adjacency matrix
   for v1, v2, d in shortcuts:
      x = nodes.index(v1)
      y = nodes.index(v2)
      graph[x][y] = d
      graph[y][x] = d

   # Determine the start and stop indices
   source = nodes.index(start)
   sink = nodes.index(stop)

   return (source, sink, graph)


# Perform a depth-first search from the source
# to the sink to determine the longest path.
def dfs(graph, v1, sink, distance, old_visited):
   # Since the set of visited nodes differs from
   # path to path, we must make a copy of it so
   # that modifications don't affect other paths.
   visited = old_visited.copy()
   visited.add(v1)

   # If the current node is the sink, then end
   # this path.
   if v1 == sink:
      return distance

   # Follow each path from the current node, and
   # save the distance of that path.
   distances = [ 0 ]
   for v2 in range(len(graph[v1])):
      if (graph[v1][v2] > 0) and (v2 not in visited):
         new_distance = distance + graph[v1][v2]
         # Recurse along the path through each neighbor
         distances.append(dfs(graph, v2, sink, new_distance, visited))

   # Return the longest distance from this node
   # to the sink.
   return max(distances)
      

   
if __name__ == '__main__':
   start_time = time.time()
   # Read in the file and organize the data
   trails = readFile("input23b.txt")

   # Define the start and stop points
   start = (0, 1)
   stop = (len(trails) - 1, len(trails) - 2)

   print('building nodes')
   nodes, adjacencies = buildNodes(trails, start, stop)

   print('building paths')
   shortcuts = buildPaths(trails, nodes, adjacencies)

   print('building graph')
   source, sink, graph = buildGraph(shortcuts, adjacencies, start, stop)

   print('calculating distance')
   distance = dfs(graph, source, sink, 0, set())
   print('distance = ' + str(distance))
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
   
