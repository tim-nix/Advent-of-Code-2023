# This solution uses Karger's algorithm to determine
# the minimum cut set of the graph.
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
# However, in this case, each stored edge is a tuple
# containing both vertices of the edge.
def parseInput(lines):
   graph = dict()
   for line in lines:
      node, edges = line.split(':')
      edges = edges.lstrip().split(' ')
      if node not in graph:
         graph[node] = []
         
      for edge in edges:
         graph[node].append((node, edge))
         if edge not in graph:
            graph[edge] = [ (edge, node) ]
         else:
            graph[edge].append((edge, node))

   return graph


# Repeatedly contract two nodes into a single node
# until only two nodes remain. The edges between
# the two nodes constitute the cut set.
def contract(graph1):
   # Make a deep copy of the graph. We need to do
   # this to preserve the original graph as we
   # may need to execute this function repeatedly
   # until the min cut set is generated.
   print('copying graph')
   graph2 = dict()
   for key in graph1:
      for value in graph1[key]:
         if key not in graph2:
            graph2[key] = [ value ]
         else:
            graph2[key].append(value)

   print('contracting')
   # Keep contracting until only two nodes remain
   while len(graph2.keys()) > 2:
      # Generate list of nodes
      nodes = list(graph2.keys())
      
      # Generate list of edges from the current set
      # of nodes. This set of edges will allow the
      # uniform, random selection of an edge from
      # the collection of edges.
      edges = []
      for key in graph2:
         for edge1, edge2 in graph2[key]:
            if edge1 not in key:
               search_edge = edge1
            elif edge2 not in key:
               search_edge = edge2

            possibles = [ nodes[i] for i in range(len(nodes)) if search_edge in nodes[i] ]
            if len(possibles) > 0:
               found_edge = possibles[0]
            
         edges.append((key, found_edge))

      # Select a random edge.
      node1, node2 = random.choice(edges)

      # Combine the two nodes of the edge into a single node.
      # Separate the names by a comma to prevent mismatching
      # of the original node labels with the concatenation
      # of the newnode label (e.g., 'ssl' in 'qrs,slp' vs
      # 'ssl' in 'qrsslp').
      newnode = node1 + ',' + node2
      graph2[newnode] = []
      
      # Iterate through the list of edges from node1, and if
      # it is not a self-loop, then add it as an edge to
      # newnode.
      for edge1, edge2 in graph2[node1]:
         if (edge1 not in newnode) and (edge2 not in newnode):
            print('neither end is rooted')
         elif (edge1 in newnode) and (edge2 not in newnode):
            graph2[newnode].append((edge1, edge2))
         elif (edge2 in newnode) and (edge1 not in newnode):
            graph2[newnode].append((edge2, edge1))

      # Delete node1 from the graph.
      del graph2[node1]

      # Iterate through the list of edges from node2, and if
      # it is not a self-loop, then add it as an edge to
      # newnode.
      for edge1, edge2 in graph2[node2]:
         if (edge1 not in newnode) and (edge2 not in newnode):
            print('neither end is rooted')
         elif (edge1 in newnode) and (edge2 not in newnode):
            graph2[newnode].append((edge1, edge2))
         elif (edge2 in newnode) and (edge1 not in newnode):
            graph2[newnode].append((edge2, edge1))

      # Delete node2 from the graph.
      del graph2[node2]

   # Return the resulting graph.
   return graph2
      


if __name__ == '__main__':
   start_time = time.time()
   # Read in the file and organize the data.
   lines = readFile("input25b.txt")
   graph = parseInput(lines)

   # Since we know that the size of the cut set is 3,
   # repeat the process until a cut set of size 3 is
   # found.
   done = False
   while not done:
      graph2 = contract(graph)
      nodes = list(graph2.keys())
      if len(graph2[nodes[0]]) == 3:
         done = True
         length1 = len(nodes[0].replace(',', '')) // 3
         length2 = len(nodes[1].replace(',', '')) // 3
         print('results = ' + str(length1 * length2))

   print("\n\n--- %s seconds ---" % (time.time() - start_time))
         


   
   
   
   
               
   

   
