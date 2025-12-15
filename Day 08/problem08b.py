# Using multiple starting locations, determine the
# number of steps needed so that, if all paths were
# followed simultaneously until all paths reach a
# destination in the same number of steps. The
# solution is not tractable if all paths are
# followed simultaneously repeatedly until all paths
# reach a distination. Therefore, for each path, we
# determine the cycle size; that is, the number of
# steps needed for a single path the reach its
# destination. Then, the least common multiple is
# calculated to determine the total needed steps.
import time
from math import gcd

# Read in the data file and convert it to a list
# of strings.
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


# Separate the input into the directions (steps)
# and the map.  The directions consist of a list
# of characters ('R' and 'L') with 'R' corresponding
# to a step to the right and 'L' corresponding to
# a step to the left. The map is a dictionary
# in which the index is the 'from' location and
# the value is the 'to' locations (two locations
# corresponding to a step left and a step right)
# stored as a tuple.
def parseInput(lines):
   desert_map = {}
   steps = list(lines[0])
   for index in range(2, len(lines)):
      direction = lines[index].split('=')
      start = direction[0].strip()
      choices = direction[1].split(',')
      left = choices[0][2:]
      right = choices[1][1:4]

      desert_map[start] = (left, right)

   return (steps, desert_map)


# Build a list of all starting locations; that is,
# all locations that end with an 'A'.
def genStart(locations):
   start = []
   for loc in locations:
      #print(loc)
      if loc[2] == 'A':
        start.append(loc)

   return start


if __name__ == '__main__':
   start_time = time.time()
   lines = readFile("input8b.txt")
   steps, desert_map = parseInput(lines)

   # Generate the collection of starting locations
   # as a list.
   locations = genStart(desert_map.keys())

   # For each starting location, repeatedly follow
   # the directions until the destination is reached
   # (any location that ends in a 'Z').  Determine
   # how many steps it took and store this value.
   cycles = []
   for location in locations:
      num_steps = 0
      done = False
      loc = location
      while not done:
         for step in steps:
            if step == 'L':
               loc = desert_map[loc][0]
            elif step == 'R':
               loc = desert_map[loc][1]
            else:
               print('Error: unknown step: ' + step)
            num_steps += 1
            # Once the destination is reached, record the
            # number of steps needed and follow the next
            # path (if it exists).
            if loc[2] == 'Z':
               #print('found the end in ' + str(num_steps) + ' steps.')
               cycles.append(num_steps)
               done = True
               break

   # Given these cycle sizes, determin the least common
   # multiple.  The LCM will be the number of steps needed
   # for all paths to reach their destination at the same
   # time and display the results.
   #print('cycles = ' + str(cycles))
   lcm = 1
   for i in cycles:
      lcm = lcm * i // gcd(lcm, i)

   print('number of steps = ' + str(lcm))
   
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

   
