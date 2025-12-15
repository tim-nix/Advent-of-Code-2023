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

# Translate the 'RGB' color into the direction
# and distance.  The first five hexadecimal
# digits encode the distance in meters as a
# five-digit hexadecimal number. The last
# hexadecimal digit encodes the direction to
# dig: 0 means R, 1 means D, 2 means L, and
# 3 means U. 
def parseInput(lines):
   direction = [ 'R', 'D', 'L', 'U' ]
   dig_plan = []
   for line in lines:
      dig_plan.append(line.split())

   for i in range(len(dig_plan)):
      # Pull out the 'RGB color'
      instruction = dig_plan[i][2]
      # Pull out the distance and prepend '0x'
      # to it (as a hexidecimal number).
      distance = '0x' + instruction[2:7]
      # Convert the hexidecimal number to an
      # integer.
      distance = int(distance, 0)
      # Pull out the direction digit and
      # convert it to the character representative.
      dir_i = int(instruction[7])
      dig_plan[i] = [ direction[dir_i], distance ]
      
   return dig_plan 

      
if __name__ == '__main__':
   lines = readFile("input18b.txt")
   dig_plan = parseInput(lines)
   
   dig_locations = []
   boundary_points = 0
   current_x, current_y = 0, 0
   dig_locations.append((current_x, current_y))
   # Add boundary dig locations to set
   # Convert the direction into the delta x and
   # delta y for each newly dug square meter.
   for step in dig_plan:
      match step[0]:
         case 'R':
            step_x = 1
            step_y = 0
         case 'L':
            step_x = -1
            step_y = 0
         case 'U':
            step_x = 0
            step_y = 1
         case 'D':
            step_x = 0
            step_y = -1
         case _:
            print('Unknown direction ' + step[0])

      # Add the next set of coordinates to the set of
      # dig locations.
      current_x += step_x * step[1]
      current_y += step_y * step[1]
      boundary_points += step[1]
      dig_locations.append((current_x, current_y))

   up = 0
   down = 0
   # Use the shoelace formula to calculate the inside area
   # (only includes a portion of each boundary location)
   for p_i in range(len(dig_locations) - 1):
      up += dig_locations[p_i][0] * dig_locations[p_i + 1][1]
      down += dig_locations[p_i][1] * dig_locations[p_i + 1][0]
   total = abs(up - down) // 2

   up = 0
   down = 0
   # Use the shoelace formula to calculate the inside area
   # (only includes a portion of each boundary location)
   for p_i in range(len(dig_locations) - 1):
      # Multiply the x coordinate of each vertex by the y
      # coordinate of the next vertex. Add the results.
      up += dig_locations[p_i][0] * dig_locations[p_i + 1][1]
      # Multiply the y coordinate of each vertex by the x
      # coordinate of the next vertex. Again, add these results.
      down += dig_locations[p_i][1] * dig_locations[p_i + 1][0]
   # Subtract the sum of the second products from the sum of the
   # first products and divide this difference by 2.
   total = abs(up - down) // 2

   # Use Pick's formula to add back the missing area.
   interior_points = total - (boundary_points // 2) + 1
   print('interior points = ' + str(interior_points))
   print('number of boundary positions = ' + str(boundary_points))
   area = interior_points + boundary_points
   print('total volume = ' + str(area) + ' cubic meters.')
   

   
   

   
