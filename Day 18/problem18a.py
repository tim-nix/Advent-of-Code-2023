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


# Turn the file input into a list of lists.
# Each inner list corresponds to a single dig
# instruction with the first element being the
# direction (U, D, L, R), the second element
# being the distance (expressed as an integer),
# and the third element being the RGB color
# (represented as a string, starting with #)
def parseInput(lines):
   dig_plan = []
   for line in lines:
      dig_plan.append(line.split())

   for i in range(len(dig_plan)):
      dig_plan[i][1] = int(dig_plan[i][1])
      dig_plan[i][2] = dig_plan[i][2][1:-1]
      
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
   
   
   

   
