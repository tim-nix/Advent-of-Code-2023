# This solution determines the longest, shortest
# path for each vertex. The most traversed edge
# is then removed from the graph. The process
# is repeated until the graph partitions.  The
# size of the partitions are then determined
# for calculation of the answer (their product).
import random
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


# From the file input, generate an adjacency list.
def parseInput(lines):
   graph = dict()
   for line in lines:
      node, edges = line.split(':')
      edges = edges.lstrip().split(' ')
      if node not in graph:
         graph[node] = []
         
      for edge in edges:
         graph[node].append(edge)
         if edge not in graph:
            graph[edge] = [ node ]
         else:
            graph[edge].append(node)

   return graph


# Finds the shortest path from the start node to
# to the stop node.  The algorithm uses BFS to
# do this since the graph is undirected, unweighted.
def findShortestPath(graph, start, stop):
   toVisit = [ start ]
   visited = set()
   parent = dict()
   parent[start] = start
   # Continue to visit nodes as long as there are
   # nodes to visit.
   while len(toVisit) > 0:
      current = toVisit.pop(0)
      if current in visited:
         continue
      
      visited.add(current)
      # If the current node is the stop node
      # then stop searching.
      if current == stop:
         break

      for other in graph[current]:
         if other not in visited:
            toVisit.append(other)
            parent[other] = current

   # Generate the path from the stop node back
   # to the start node.
   path = [ stop ]
   current = stop
   done = False
   while not done:
      current = parent[current]
      path.append(current)
      if current == start:
         done = True

   # Return the path
   return path
            

# Determine the most traversed edge in the graph within
# the longest, shortest paths for each node. The longest,
# shortest path is the shortest path between a given node
# and the shortest paths between that node and all other
# nodes.  The assumption is that the most traversed node(s)
# are part of the minimum cut set.
def getMaxEdge(graph):
   traverse_count = dict()
   
   # For each distinct pair of nodes, calculate shortest path
   nodes = list(graph.keys())
   for node1 in nodes:
      longest_shortest = []
      for node2 in nodes:
         if node1 == node2:
            continue
         
         path = findShortestPath(graph, node1, node2)
         if len(path) > len(longest_shortest):
            longest_shortest = path
   
      # Increment count for each edge in path
      for j in range(len(longest_shortest) - 1):
         edge1 = (longest_shortest[j], longest_shortest[j + 1])
         edge2 = (longest_shortest[j + 1], longest_shortest[j])
         if (edge1 not in traverse_count) and (edge2 not in traverse_count):
            traverse_count[edge1] = 1
         elif edge1 in traverse_count:
            traverse_count[edge1] += 1
         else:
            traverse_count[edge2] += 1
         
   # Return edge with highest count
   max_count = 0
   max_edge = None
   for key in traverse_count:
      if traverse_count[key] > max_count:
         max_count = traverse_count[key]
         max_edge = key

   return max_edge


# Generate a list of sizes for each component
# within the graph.
def getComponentSizes(graph):
   nodes = list(graph.keys())

   sizes = []
   # Keep checking until every node is visited.
   while len(nodes) > 0:
      # Conduct a BFS from the start node to all
      # reachable nodes.
      start = nodes[0]
      toVisit = [ start ]
      visited = set()
      while len(toVisit) > 0:
         current = toVisit.pop(0)
         if current in visited:
            continue
         
         visited.add(current)
         nodes.remove(current)
         for edge in graph[current]:
            if edge not in visited:
               toVisit.append(edge)

      # The size of the component is the same
      # size as the set of visited nodes.
      sizes.append(len(visited))

   return sizes
         

if __name__ == '__main__':
   start_time = time.time()
   # Read in the file and organize the data.
   lines = readFile("input25b.txt")
   graph = parseInput(lines)

   done = False
   # Keep going until the graph is partitioned.
   while not done:
      # Find the most traversed edge from all
      # of the longest, shortest paths.
      node1, node2 = getMaxEdge(graph)
      print((node1, node2))

      # Remove the edge
      graph[node1].remove(node2)
      graph[node2].remove(node1)

      # Determine the sizes of the components.
      sizes = getComponentSizes(graph)
      
      # If there are more than 1 component, then done.
      if len(sizes) > 1:
         print('results = ' + str(sizes[0] * sizes[1]))
         done = True
         

   print("\n\n--- %s seconds ---" % (time.time() - start_time))
         


   
   
   
   
               
   

   
