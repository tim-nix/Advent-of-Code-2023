# This solution uses the networkx library to determine
# the minimum cut set of the graph.
import networkx
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
         graph[node] = edges
      else:
         graph[node].extend(edges)

   return graph




if __name__ == '__main__':
   start_time = time.time()
   # Read in the file and organize the data.
   lines = readFile("input25b.txt")

   # Generate the adjacency list (dictionary)
   graph = parseInput(lines)

   # Create a networkx graph.
   lib_graph = networkx.Graph()

   # For each edge in the adjacency list,
   # add two edges to the graph since it
   # is not directed.
   for node1 in graph:
      for node2 in graph[node1]:
         lib_graph.add_edge(node1, node2)
         lib_graph.add_edge(node2, node1)

   # Determine the minimum cut edges.
   min_cut = networkx.minimum_edge_cut(lib_graph)

   # Remove those edges from the graph.
   lib_graph.remove_edges_from(min_cut)

   # Generate the two resulting components.
   components = list(networkx.connected_components(lib_graph))

   # The answer is the product of the sizes of the two
   # components.
   print('result = ' + str(len(components[0]) * len(components[1])))

   print("\n\n--- %s seconds ---" % (time.time() - start_time))
         
         

   
   
   
               
   

   
