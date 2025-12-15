import time
import heapq

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


# Convert the list of strings into a list of lists.
# Each string of digits is converted into a list of
# digits and each digit is converted into an integer.
def parseInput(lines):
   return [ [ int(i) for i in line] for line in lines ]


# This function uses a modified form of Dijkstra's
# algorithm to find the shortest path from the 'start'
# coordinates to the 'stop' coordinates (in this case,
# 'shortest' means the route with the minimal heat sink).
# Since the path cannot travel less than 4 steps forward
# or more than 10 steps forward in a given direction,
# the set of visited must include both the directon of
# travel and the number of steps taken in that direction.
def shortestPath(block, start, stop):
   max_distance = len(block) * len(block[0]) * 10
   minheap = []
   visited = set()

   # The minheap is a heap of nodes yet to visit.
   # The first element is the heat loss to the node.
   # The second and third elements are the x and y
   # coordinates of the node.  The fourth element is
   # the direction (initialized to 'none' for the
   # start node.  The last element is the number of
   # steps taken in the current direction.
   heapq.heappush(minheap, (0, start[0], start[1], 'none', 0))

   # Keep visiting nodes as long as there are nodes to visit.
   while (len(minheap)> 0):
      # Find node with smallest value that has not been visited.
      current = heapq.heappop(minheap)

      # If the current node has already been visited, it does not
      # need to be revisited (so skip it and move on).
      if (current[1], current[2], current[3], current[4]) not in visited:
         x, y = current[1], current[2]

         # If the current node is the 'stop' location, then we are done.
         if (x, y) == stop:
            return current[0]

         # Add the current node to the set of visited nodes.  In this
         # case, we need to also track the direction (third element)
         # and the number of steps taken in the current direction
         # (fourth element).
         visited.add((current[1], current[2], current[3], current[4]))

         # For convenience, set up a list of neighboring nodes. We use
         # the representation of the provided input and not an adjacency
         # matrix or adjacency list.
         neighbors = [ (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1) ]
         n_direction = [ 'north', 'south', 'west', 'east' ]

         # Modify the list of neighbors to exclude those that cannot be
         # traveled to from the current node because it either reverses
         # the directon or results in less than 4 steps or more than 10
         # steps in the same direction (both of which are illegal).
         if current[3] == 'north':
            neighbors.pop(1)        # remove 'south'
            n_direction.pop(1)
            if current[4] < 4:      # if have not moved 4 forward:
               neighbors.pop(1)     # remove left and right
               n_direction.pop(1)
               neighbors.pop(1)
               n_direction.pop(1)
            elif current[4] == 10:  # if have moved 10 forward:
               neighbors.pop(0)     # remove forward
               n_direction.pop(0)
         elif current[3] == 'south':
            neighbors.pop(0)        # remove 'north'
            n_direction.pop(0)
            if current[4] < 4:
               neighbors.pop(1)
               n_direction.pop(1)
               neighbors.pop(1)
               n_direction.pop(1)
            elif current[4] == 10:
               neighbors.pop(0)
               n_direction.pop(0)
         elif current[3] == 'east':
            neighbors.pop(2)        # remove 'west'
            n_direction.pop(2)
            if current[4] < 4:
               neighbors.pop(0)
               n_direction.pop(0)
               neighbors.pop(0)
               n_direction.pop(0)
            elif current[4] == 10:
               neighbors.pop(2)
               n_direction.pop(2)
         elif current[3] == 'west':
            neighbors.pop(3)        # remove 'east'
            n_direction.pop(3)
            if current[4] < 4:
               neighbors.pop(0)
               n_direction.pop(0)
               neighbors.pop(0)
               n_direction.pop(0)
            elif current[4] == 10:
               neighbors.pop(2)
               n_direction.pop(2)

         # For each remaining neighbor, if it is a legal neighbor
         # (is within the bounds of the block) and it has not been
         # visited, then add it to the minheap.  Also, check to see
         # if the neighbor is the stop location and add the path
         # state to the 'final' list.
         for n_i in range(len(neighbors)):
            n_x, n_y = neighbors[n_i]
            if (0 <= n_x < len(block)) and (0 <= n_y < len(block[0])):
               n = neighbors[n_i]
               if current[3] == n_direction[n_i]:
                  neighbor = (n[0], n[1], current[3], current[4] + 1)
               else:
                  neighbor = (n[0], n[1], n_direction[n_i], 1)

               # Check each neighbor that has not already been visited
               if neighbor not in visited:
                  # Calculate the distance to the neighbor from the current node
                  distance = current[0] + block[neighbor[0]][neighbor[1]]
                  #print('distance to neighbor = ' + str(distance))
                  heapq.heappush(minheap, (distance, neighbor[0], neighbor[1], neighbor[2], neighbor[3]))


      
if __name__ == '__main__':
   start_time = time.time()
   lines = readFile("input17b.txt")
   block = parseInput(lines)

   # The start node is the top, left node.
   start = (0, 0)

   # The destination is the bottom, right node.
   stop = (len(block) - 1, len(block[0]) - 1)

   # Call the function the determine the heat loss.
   final = shortestPath(block, start, stop)

   # Display the result
   print('minimal heat loss = ' + str(final))
   
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

   
