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
   newUniverse = []
   # expand rows
   for row in universe:
      newUniverse.append(row)
      if '#' not in row:
         newUniverse.append([ '.' for i in range(len(row)) ])
      
   # expand columns
   column = 0
   while column < len(newUniverse):
      isEmpty = True
      for row in range(len(newUniverse)):
         if newUniverse[row][column] == '#':
            isEmpty = False

      # if column is empty, add new column
      if isEmpty:
         for row in range(len(newUniverse)):
            newUniverse[row].insert(column + 1, '.')
         column += 2
      else:
         column += 1
   
   return newUniverse


def getGalaxies(universe):
   galaxies = []
   for row in range(len(universe)):
      for column in range(len(universe[row])):
         if universe[row][column] == '#':
            galaxies.append((row, column))

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
   # expand the empty rows and columns of the universe
   universe = expandUniverse(universe)
   # find the locations of the galaxies
   galaxies = getGalaxies(universe)
   # calculate all of the shortest distances
   distances = calcDistances(galaxies)
   # sum up all the distances and divide by 2
   # (each distance is double counted)
   sum_distances = sum(distances) / 2
   
   print('sum of distances = ' + str(sum_distances))
   
