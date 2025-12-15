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
   path_set = set()
   path_set.add(start)
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
         print("Only one connection found.")
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
            print("Two connections found, but neither are new.")
            path.append(start)
      else:
         print("Error: more than 2 connections.")
         done = True
   print('path found')
   
   # Replace junk pipe
   for i in range(len(pipes)):
      for j in range(len(pipes[i])):
         if (i, j) not in path_set:
            pipes[i][j] = '.'
   print('junk replaced')
   #for line in pipes:
   #   print(''.join(line))
   #print()

   # mind the gap (by widening it)
   # first generate the rows
   new_pipes = []
   for i in range(len(pipes)):
      new_row = []
      new_row.append(pipes[i][0])
      for j in range(len(pipes[i]) - 1):
         if (pipes[i][j] == '|') and (pipes[i][j + 1] == '|'):
            new_row.append('.')
            new_row.append('|')
         elif (pipes[i][j] == '|') and (pipes[i][j + 1] == 'L'):
            new_row.append('.')
            new_row.append('L')
         elif (pipes[i][j] == '|') and (pipes[i][j + 1] == 'F'):
            new_row.append('.')
            new_row.append('F')
         elif (pipes[i][j] == '|') and (pipes[i][j + 1] == '.'):
            new_row.append('.')
            new_row.append('.')
         elif (pipes[i][j] == '|') and (pipes[i][j + 1] == 'S'):
            new_row.append('.')
            new_row.append('S')
         elif (pipes[i][j] == '-') and (pipes[i][j + 1] == '-'):
            new_row.append('-')
            new_row.append('-')
         elif (pipes[i][j] == '-') and (pipes[i][j + 1] == 'J'):
            new_row.append('-')
            new_row.append('J')
         elif (pipes[i][j] == '-') and (pipes[i][j + 1] == '7'):
            new_row.append('-')
            new_row.append('7')
         elif (pipes[i][j] == '-') and (pipes[i][j + 1] == 'S'):
            new_row.append('-')
            new_row.append('S')
         elif (pipes[i][j] == 'L') and (pipes[i][j + 1] == '-'):
            new_row.append('-')
            new_row.append('-')
         elif (pipes[i][j] == 'L') and (pipes[i][j + 1] == 'J'):
            new_row.append('-')
            new_row.append('J')
         elif (pipes[i][j] == 'L') and (pipes[i][j + 1] == '7'):
            new_row.append('-')
            new_row.append('7')
         elif (pipes[i][j] == 'L') and (pipes[i][j + 1] == 'S'):
            new_row.append('-')
            new_row.append('S')
         elif (pipes[i][j] == 'J') and (pipes[i][j + 1] == '|'):
            new_row.append('.')
            new_row.append('|')
         elif (pipes[i][j] == 'J') and (pipes[i][j + 1] == 'L'):
            new_row.append('.')
            new_row.append('L')
         elif (pipes[i][j] == 'J') and (pipes[i][j + 1] == 'F'):
            new_row.append('.')
            new_row.append('F')
         elif (pipes[i][j] == 'J') and (pipes[i][j + 1] == '.'):
            new_row.append('.')
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i][j + 1] == 'S'):
            new_row.append('.')
            new_row.append('S')
         elif (pipes[i][j] == '7') and (pipes[i][j + 1] == '|'):
            new_row.append('.')
            new_row.append('|')
         elif (pipes[i][j] == '7') and (pipes[i][j + 1] == 'L'):
            new_row.append('.')
            new_row.append('L')
         elif (pipes[i][j] == '7') and (pipes[i][j + 1] == 'F'):
            new_row.append('.')
            new_row.append('F')
         elif (pipes[i][j] == '7') and (pipes[i][j + 1] == '.'):
            new_row.append('.')
            new_row.append('.')
         elif (pipes[i][j] == '7') and (pipes[i][j + 1] == 'S'):
            new_row.append('.')
            new_row.append('S')
         elif (pipes[i][j] == 'F') and (pipes[i][j + 1] == '-'):
            new_row.append('-')
            new_row.append('-')
         elif (pipes[i][j] == 'F') and (pipes[i][j + 1] == 'J'):
            new_row.append('-')
            new_row.append('J')
         elif (pipes[i][j] == 'F') and (pipes[i][j + 1] == '7'):
            new_row.append('-')
            new_row.append('7')
         elif (pipes[i][j] == 'F') and (pipes[i][j + 1] == 'S'):
            new_row.append('-')
            new_row.append('S')
         elif (pipes[i][j] == '.') and (pipes[i][j + 1] == '|'):
            new_row.append('.')
            new_row.append('|')
         elif (pipes[i][j] == '.') and (pipes[i][j + 1] == 'L'):
            new_row.append('.')
            new_row.append('L')
         elif (pipes[i][j] == '.') and (pipes[i][j + 1] == 'F'):
            new_row.append('.')
            new_row.append('F')
         elif (pipes[i][j] == '.') and (pipes[i][j + 1] == '.'):
            new_row.append('.')
            new_row.append('.')
         elif (pipes[i][j] == '.') and (pipes[i][j + 1] == 'S'):
            new_row.append('.')
            new_row.append('S')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == '|'):
            new_row.append('.')
            new_row.append('|')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == '-'):
            new_row.append('-')
            new_row.append('-')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == 'L'):
            new_row.append('.')
            new_row.append('L')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == 'J'):
            new_row.append('-')
            new_row.append('J')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == '7'):
            new_row.append('-')
            new_row.append('7')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == 'F'):
            new_row.append('.')
            new_row.append('F')
         elif (pipes[i][j] == 'S') and (pipes[i][j + 1] == '.'):
            new_row.append('.')
            new_row.append('.')
         else:
            print('missing row case...' + str((pipes[i][j], pipes[i][j + 1])))
      new_pipes.append(new_row)

   pipes = new_pipes
   #for line in pipes:
   #   print(line)
   #print()

   # now generate the extra rows based on column values
   new_pipes = [ pipes[0] ]
   for i in range(len(pipes) - 1):
      new_row = []
      for j in range(len(pipes[i])):
         if (pipes[i][j] == '|') and (pipes[i + 1][j] == '|'):
            new_row.append('|')
         elif (pipes[i][j] == '|') and (pipes[i + 1][j] == 'L'):
            new_row.append('|')
         elif (pipes[i][j] == '|') and (pipes[i + 1][j] == 'J'):
            new_row.append('|')
         elif (pipes[i][j] == '|') and (pipes[i + 1][j] == 'S'):
            new_row.append('|')
         elif (pipes[i][j] == '-') and (pipes[i + 1][j] == '-'):
            new_row.append('.')
         elif (pipes[i][j] == '-') and (pipes[i + 1][j] == '7'):
            new_row.append('.')
         elif (pipes[i][j] == '-') and (pipes[i + 1][j] == 'F'):
            new_row.append('.')
         elif (pipes[i][j] == '-') and (pipes[i + 1][j] == '.'):
            new_row.append('.')
         elif (pipes[i][j] == '-') and (pipes[i + 1][j] == 'S'):
            new_row.append('.')
         elif (pipes[i][j] == 'L') and (pipes[i + 1][j] == '-'):
            new_row.append('.')
         elif (pipes[i][j] == 'L') and (pipes[i + 1][j] == '7'):
            new_row.append('.')
         elif (pipes[i][j] == 'L') and (pipes[i + 1][j] == 'F'):
            new_row.append('.')
         elif (pipes[i][j] == 'L') and (pipes[i + 1][j] == '.'):
            new_row.append('.')
         elif (pipes[i][j] == 'L') and (pipes[i + 1][j] == 'S'):
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i + 1][j] == '-'):
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i + 1][j] == '7'):
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i + 1][j] == 'F'):
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i + 1][j] == '.'):
            new_row.append('.')
         elif (pipes[i][j] == 'J') and (pipes[i + 1][j] == 'S'):
            new_row.append('.')
         elif (pipes[i][j] == '7') and (pipes[i + 1][j] == '|'):
            new_row.append('|')
         elif (pipes[i][j] == '7') and (pipes[i + 1][j] == 'L'):
            new_row.append('|')
         elif (pipes[i][j] == '7') and (pipes[i + 1][j] == 'J'):
            new_row.append('|')
         elif (pipes[i][j] == '7') and (pipes[i + 1][j] == 'S'):
            new_row.append('|')
         elif (pipes[i][j] == 'F') and (pipes[i + 1][j] == '|'):
            new_row.append('|')
         elif (pipes[i][j] == 'F') and (pipes[i + 1][j] == 'L'):
            new_row.append('|')
         elif (pipes[i][j] == 'F') and (pipes[i + 1][j] == 'J'):
            new_row.append('|')
         elif (pipes[i][j] == 'F') and (pipes[i + 1][j] == 'S'):
            new_row.append('|')
         elif (pipes[i][j] == '.') and (pipes[i + 1][j] == '-'):
            new_row.append('.')
         elif (pipes[i][j] == '.') and (pipes[i + 1][j] == '7'):
            new_row.append('.')
         elif (pipes[i][j] == '.') and (pipes[i + 1][j] == 'F'):
            new_row.append('.')
         elif (pipes[i][j] == '.') and (pipes[i + 1][j] == '.'):
            new_row.append('.')
         elif (pipes[i][j] == '.') and (pipes[i + 1][j] == 'S'):
            new_row.append('.')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == '|'):
            new_row.append('|')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == '-'):
            new_row.append('.')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == 'L'):
            new_row.append('|')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == 'J'):
            new_row.append('|')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == '7'):
            new_row.append('.')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == 'F'):
            new_row.append('.')
         elif (pipes[i][j] == 'S') and (pipes[i + 1][j] == '.'):
            new_row.append('.')
         else:
            print('missing column case...' + str((pipes[i][j], pipes[i + 1][j])))
            print('i = ' + str(i) + ' and j = ' + str(j))
            
      new_pipes.append(new_row)
      new_pipes.append(pipes[i + 1])
   pipes = new_pipes
      
   # Set all open locations connected to outside
   done = False
   while not done:
      done = True
      for i in range(len(pipes)):
         for j in range(len(pipes[i])):
            if pipes[i][j] == '.':
               if (i in [ 0, len(pipes) - 1 ]) or (j in [ 0, len(pipes[i]) - 1 ]):
                  pipes[i][j] = '0'
                  done = False
               elif (i - 1 >= 0) and (pipes[i - 1][j] == '0'):
                  pipes[i][j] = '0'
                  done = False
               elif (j - 1 >= 0) and (pipes[i][j - 1] == '0'):
                  pipes[i][j] = '0'
                  done = False
               elif (i + 1 < len(pipes)) and (pipes[i + 1][j] == '0'):
                  pipes[i][j] = '0'
                  done = False
               elif (j + 1 < len(pipes[i])) and (pipes[i][j + 1] == '0'):
                  pipes[i][j] = '0'
                  done = False

   # Now, reduce the map back to original size

   new_pipes = []
   for i in range(0, len(pipes), 2):
      new_row = []
      for j in range(0, len(pipes[i]), 2):
         new_row.append(pipes[i][j])
      new_pipes.append(new_row)

   pipes = new_pipes
   #for line in pipes:
   #   print(''.join(line[:100]))
   #print()

   # Count the open spaces
   print('353 is too high')
   count = 0
   for line in pipes:
      count += line.count('.')
   print('count = ' + str(count))


   
   
