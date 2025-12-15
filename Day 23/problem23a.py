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


# Find the longest hiking path by following the current
# path as long as it does not branch.  If the path
# branches, then recurse down each path and choose the
# longest path.
def findLongestHike(trails, current, stop, old_visited):
   # Make a copy of the visited set to allow for
   # backtracking at higher recursion levels.
   visited = set()
   for val in old_visited:
      visited.add(val)

   # Test each possible neighbor location from the
   # current location
   deltas = [ (0, -1), (0, 1), (-1, 0), (1, 0) ]
   toVisit = [ current ]
   path = []
   # If there is only one path, then follow it.
   while len(toVisit) == 1:
      x, y = toVisit.pop(0)
      visited.add((x, y))
      path.append((x, y))
      
      if (x, y) == stop:
         #print('found the end')
         continue
      
      if trails[x][y] == '>':
         #print('handling > at ' + str((x, y)))
         toVisit.append((x, y + 1))

      elif trails[x][y] == 'v':
         #print('handling v at ' + str((x, y)))
         toVisit.append((x + 1, y))

      else:
         for delta_x, delta_y in deltas:
            if ((0 <= (x + delta_x) < len(trails)) and
                (0 <= (y + delta_y) < len(trails[x]))):
               if (((x + delta_x, y + delta_y) not in visited) and
                   (trails[x + delta_x][y + delta_y] != '#')):
                  if (((delta_x, delta_y) == (0, -1)) and
                      (trails[x + delta_x][y + delta_y] == '>')):
                     continue

                  if (((delta_x, delta_y) == (-1, 1)) and
                      (trails[x + delta_x][y + delta_y] == '>')):
                     continue

                  toVisit.append((x + delta_x, y + delta_y))

   # If there are no more paths, then return to the
   # higher recursion level
   if len(toVisit) == 0:
      return path

   # If there are multiple paths from the current location,
   # then follow each recursively.  Afterwards, choose the
   # longest path and return it.
   from_here = []
   for p in toVisit:
      new_path = findLongestHike(trails, p, stop, visited)
      if len(new_path) > len(from_here):
         from_here = new_path

   return path + from_here
      
   

if __name__ == '__main__':
   # Read in the file and organize the data
   trails = readFile("input23b.txt")

   # Define the start and stop points
   start = (0, 1)
   stop = (len(trails) - 1, len(trails) - 2)

   # Find the longest hiking path
   path = findLongestHike(trails, start, stop, set())

   # Print out the resulting distance
   print('distance = ' + str(len(path) - 1))
   
   
   
   
