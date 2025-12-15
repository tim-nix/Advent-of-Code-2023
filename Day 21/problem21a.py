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

# Convert the input from a list of string to
# a list of lists of characters. So, each
# single character represents a location on
# the map.
def parseInput(lines):
   area_map = []
   for line in lines:
      area_map.append(list(line))

   return area_map


# This solution is a straight forward, brute
# force.  It uses two maps that are, initially,
# copies of each other.  The start location is
# found and replaced with zero.  Then, the main
# map is traversed (for each step) and if the
# location contains the previous step number,
# the map copy is modified so that any non-
# rock neighbors of the previous step location
# is marked with the current step number.  Then
# the map and the map copy are swapped, and the
# process is repeated.
if __name__ == '__main__':
   lines = readFile("input21b.txt")
   area_map = parseInput(lines)

   # Find the start location
   s = (-1, -1)
   x = 0
   done = False
   while (not done) and (x < len(area_map)):
      y = 0
      while (not done) and (y < len(area_map[x])):
         if area_map[x][y] == 'S':
            s = (x, y)
            done = True
         y += 1
      x += 1

   # Replace the start location on the map with zero
   print('start = ' + str(s))
   area_map[s[0]][s[1]] = 0

   # Make a copy of the map
   area_map2 = [ [ area_map[x][y] for y in range(len(area_map[x])) ] for x in range(len(area_map)) ]

   # Update the map copy so that, for each location
   # marked with the previous step, the non-rock
   # neighbor locations are marked with the current
   # step.
   max_steps = 64
   for step in range(1, max_steps + 1):
      #print('step ' + str(step) + ' of ' + str(max_steps))
      for x in range(len(area_map)):
         for y in range(len(area_map[x])):
            if area_map[x][y] == step - 1:
               if ((x - 1) >= 0) and (area_map[x - 1][y] != '#'):
                  area_map2[x - 1][y] = step
               if ((y - 1) >= 0) and (area_map[x][y - 1] != '#'):
                  area_map2[x][y - 1] = step
               if ((x + 1) < len(area_map)) and (area_map[x + 1][y] != '#'):
                  area_map2[x + 1][y] = step
               if ((y + 1) < len(area_map[x])) and (area_map[x][y + 1] != '#'):
                  area_map2[x][y + 1] = step

      # Swap the maps
      temp = area_map
      area_map = area_map2
      area_map2 = temp

   # Count number of max steps
   count = 0
   for x in range(len(area_map)):
      for y in range(len(area_map[x])):
         if area_map[x][y] == max_steps:
            count += 1

   # Display the results
   print('Number of locations reached = ' + str(count))
               
   
