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


def tiltSouth(surface):
   for i in range(len(surface) - 1, -1, -1):
      for j in range(len(surface[i])):
         if surface[i][j] == 'O':
            #print('moving rock at (' + str(i) + ', ' + str(j) + ')')
            k = i
            while ((k + 1) < len(surface)) and (surface[k + 1][j] == '.'):
               surface[k][j] = '.'
               surface[k + 1][j] = 'O'
               k = k + 1

def tiltEast(surface):
   for i in range(len(surface)):
      for j in range(len(surface[i]) - 1, -1, -1):
         if surface[i][j] == 'O':
            #print('moving rock at (' + str(i) + ', ' + str(j) + ')')
            k = j
            while ((k + 1) < len(surface[i])) and (surface[i][k + 1] == '.'):
               surface[i][k] = '.'
               surface[i][k + 1] = 'O'
               k = k + 1
               

def tiltWest(surface):
   for i in range(len(surface)):
      for j in range(len(surface[i])):
         if surface[i][j] == 'O':
            #print('moving rock at (' + str(i) + ', ' + str(j) + ')')
            k = j
            while ((k - 1) >= 0) and (surface[i][k - 1] == '.'):
               surface[i][k] = '.'
               surface[i][k - 1] = 'O'
               k = k - 1

def spinOnce(surface):
   tiltNorth(surface)
   tiltWest(surface)
   tiltSouth(surface)
   tiltEast(surface)
   
               
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
   #for line in surface:
   #   print(line)
   #print()

   spin_set = set()
   num_spins = 1000000000
   repeat = []
   base_i = []
   for i in range(num_spins):
      spinOnce(surface)
      im_surface = ''
      for line in surface:
         im_surface += ''.join(line)
      if im_surface in spin_set:
         #print('repeat at ' + str(i))
         if len(repeat) == 0:
            base_i = i
         repeat.append(calcLoad(surface))
         if len(repeat) == 1000:
            #print(repeat)
            break
      else:
         spin_set.add(im_surface)

   # find cycle length
   cycle_length = -1
   for i in range(2, len(repeat) // 2):
      if repeat[:i] == repeat[i:2*i]:
         cycle_length = i
         break
   if cycle_length == -1:
      print('Error: repeat not big enough')
   else:
      print('cycle_length = ' + str(cycle_length))
      print(repeat[:cycle_length])
      print('min_index = ' + str(base_i))
      print('max_index = ' + str(base_i + cycle_length))
      load_index = (num_spins - base_i - 1) % cycle_length
      print('load_index = ' + str(load_index))
      print('load = ' + str(repeat[load_index]))
   
   
   
   
