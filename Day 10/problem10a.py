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
      

def parseInput(lines):
   pipes = []
   for line in lines:
      pipes.append(list(line))

   return pipes


def findS(pipes):
   row = 0
   col = 0
   for r in range(len(pipes)):
      if 'S' in pipes[r]:
         row = r
         col = pipes[r].index('S')
         return (row, col)

   return "Error"


def findConnections(location, pipes):
   connections = []
   x, y = location
   
   # check north
   if (pipes[x][y] in [ '|', 'L', 'J', 'S' ]) and (pipes[x - 1][y] in [ '|', '7', 'F', 'S' ]): 
      connections.append((x - 1, y))

   # check east
   if (pipes[x][y] in [ '-', 'F', 'L', 'S' ]) and (pipes[x][y + 1] in [ '-', 'J', '7' ]): 
      connections.append((x, y + 1))

   # check south
   if (pipes[x][y] in [ '|', '7', 'F', 'S' ]) and (pipes[x + 1][y] in [ '|', 'L', 'J' ]): 
      connections.append((x + 1, y))

   # check west
   if (pipes[x][y] in [ '-', 'J', '7', 'S' ]) and (pipes[x][location[1] - 1] in [ '-', 'L', 'F' ]): 
      connections.append((x, y - 1))

   return connections


if __name__ == '__main__':
   lines = readFile("input10b.txt")
   pipes = parseInput(lines)
   #for line in pipes:
   #   print(line)
   #print()
   
   # Find S
   start = findS(pipes)
   print('start = ' + str(start))
   
   # Generate path (assume S is not on outside edge)
   path = []
   path_set = { start }
   current = start
   done = False
   while not done:
      #print('current = ' + str(current))
      connections = findConnections(current, pipes)
      #print('connections = ' + str(connections))
      if len(connections) == 0:
         print("Error: no connections found.")
         done = True
      elif (len(connections) == 1) and (len(path) > 1):
         done = True
         path.append(connections[0])
      elif (len(connections) == 1) or (len(connections) == 2):
         if connections[0] not in path_set:
            path_set.add(connections[0])
            path.append(connections[0])
            current = connections[0]
         elif connections[1] not in path_set:
            path_set.add(connections[1])
            path.append(connections[1])
            current = connections[1]
         else:
            done = True
            path.append(start)
      else:
         print("Error: more than 2 connections.")
         done = True
      
   # Find furtherest point (midpoint in path?)
   #print(path)
   print('path is ' + str(len(path)) + ' steps long.')
   print('furtherest distance is ' + str(len(path) // 2))

   
   
