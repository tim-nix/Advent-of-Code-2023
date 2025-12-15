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
   universe = []
   for line in lines:
      universe.append(list(line))

   return universe


def expandUniverse(universe):
   expansion_rows = []
   # expand rows
   for row in range(len(universe)):
      if '#' not in universe[row]:
         expansion_rows.append(row)

   expansion_columns = []
   # expand columns
   for column in range(len(universe[0])):
      isEmpty = True
      for row in range(len(universe)):
         if universe[row][column] == '#':
            isEmpty = False

      # if column is empty, add new column
      if isEmpty:
         expansion_columns.append(column)

   return (expansion_rows, expansion_columns)


def getGalaxies(universe, expansion, shift):
   galaxies = []

   expansionX, expansionY = expansion
   x = 0
   for row in range(len(universe)):
      y = 0
      for column in range(len(universe[row])):
         if universe[row][column] == '#':
            galaxies.append((x, y))
         if column in expansionY:
            y += shift
         else:
            y += 1
      if row in expansionX:
         x += shift
      else:
         x += 1
            

   return galaxies


def calcDistances(galaxies):
   distances = []
   for x1, y1 in galaxies:
      for x2, y2 in galaxies:
         distance = abs(x1 - x2) + abs(y1 - y2)
         if distance > 0:
            distances.append(distance)

   return distances


if __name__ == '__main__':
   lines = readFile("input11b.txt")
   universe = parseInput(lines)

   # denotes the expansion factor
   shift = 1000000
   
   # find the rows and columns which expanded
   expansion = expandUniverse(universe)
   
   # find the locations of the galaxies
   galaxies = getGalaxies(universe, expansion, shift)
   
   # calculate all of the shortest distances
   distances = calcDistances(galaxies)
   
   # sum up all the distances and divide by 2
   # (each distance is double counted)
   sum_distances = sum(distances) // 2
   
   print('sum of distances = ' + str(sum_distances))
   
