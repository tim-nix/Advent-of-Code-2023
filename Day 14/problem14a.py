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
   surface = []
   for line in lines:
      surface.append(list(line))

   return surface


def tiltNorth(surface):
   for i in range(len(surface)):
      for j in range(len(surface[i])):
         if surface[i][j] == 'O':
            #print('moving rock at (' + str(i) + ', ' + str(j) + ')')
            k = i
            while ((k - 1) >= 0) and (surface[k - 1][j] == '.'):
               surface[k][j] = '.'
               surface[k - 1][j] = 'O'
               k = k - 1


def calcLoad(surface):
   load = 0
   for i in range(len(surface)):
      for j in range(len(surface[i])):
         if surface[i][j] == 'O':
            load += len(surface) - i

   return load


if __name__ == '__main__':
   lines = readFile("input14b.txt")
   surface = parseInput(lines)
   tiltNorth(surface)
   load = calcLoad(surface)
   print('load = ' + str(load))
   
   
   
