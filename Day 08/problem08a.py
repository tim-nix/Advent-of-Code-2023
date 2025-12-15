# Determine the number of steps to travel from location
# 'AAA' to location 'ZZZ' given a set of directions (a
# sequence of left and right steps) and a map consisting
# of starting locations and resulting location if a left
# step is made and a resulting location if a right step
# is made as start = (left, right). Parse the input and
# repeatedly follow the step directions to travel from
# 'AAA' to 'ZZZ'  Display the number of steps taken.
import time

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

   # Convert the directions into a list of steps.
   steps = list(lines[0])

   # The additional data is used to build the map
   # as a dictionary.
   for index in range(2, len(lines)):
      direction = lines[index].split('=')
      start = direction[0].strip()
      choices = direction[1].split(',')
      left = choices[0][2:]
      right = choices[1][1:4]

      desert_map[start] = (left, right)

   # Return the directions and the map as a tuple.
   return (steps, desert_map)
      


if __name__ == '__main__':
   start_time = time.time()
   lines = readFile("input8b.txt")
   # Convert the input into the directions and
   # the map.
   steps, desert_map = parseInput(lines)

   # Define the staring location.
   location = 'AAA'

   # Follow the directions over and over until
   # the destination 'ZZZ' is reached. Keep track
   # of the number of steps taken.
   num_steps = 0
   while location != 'ZZZ':
      for step in steps:
         if step == 'L':
            location = desert_map[location][0]
         elif step == 'R':
            location = desert_map[location][1]
         else:
            print('Error: unknown step: ' + step)
         num_steps += 1

   # Display the number of steps taken.
   print('number of steps = ' + str(num_steps))
   
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
