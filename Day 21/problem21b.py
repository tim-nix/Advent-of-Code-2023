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


# Find the start location
def findStart(area_map):
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

   return s


def fillMap(area_map, start, steps):
   # Make two copies of the map
   area_map1 = [ [ area_map[x][y] for y in range(len(area_map[x])) ] for x in range(len(area_map)) ]
   area_map2 = [ [ area_map[x][y] for y in range(len(area_map[x])) ] for x in range(len(area_map)) ]

   area_map1[start[0]][start[1]] = 0

   for step in range(1, steps + 1):
      for x in range(len(area_map)):
         for y in range(len(area_map[x])):
            if area_map1[x][y] == step - 1:
               if ((x - 1) >= 0) and (area_map1[x - 1][y] != '#'):
                  area_map2[x - 1][y] = step
               if ((y - 1) >= 0) and (area_map1[x][y - 1] != '#'):
                  area_map2[x][y - 1] = step
               if ((x + 1) < len(area_map)) and (area_map1[x + 1][y] != '#'):
                  area_map2[x + 1][y] = step
               if ((y + 1) < len(area_map[x])) and (area_map1[x][y + 1] != '#'):
                  area_map2[x][y + 1] = step

      # Swap the maps
      temp = area_map1
      area_map1 = area_map2
      area_map2 = temp

   # Count number of max steps
   count = 0
   for x in range(len(area_map1)):
      for y in range(len(area_map1[x])):
         if area_map1[x][y] == step:
            count += 1

   return count

      
if __name__ == '__main__':
   lines = readFile("input21b.txt")
   area_map = parseInput(lines)

   start = findStart(area_map)
   print('start = ' + str(start))
   area_map[start[0]][start[1]] = '.'
   width = len(area_map)


   # Find how many steps are reached in the odd map
   odd_fill = fillMap(area_map, start, 2 * width + 1)
   print('the odd map = ' + str(odd_fill))

   # Find how many steps are reached in the even map
   even_fill = fillMap(area_map, start, 2 * width)
   print('the even map = ' + str(even_fill))

   
   max_steps = 26501365

   # Find how many maps wide are reachable within the given
   # number of steps and then find how many odd maps and
   # how many even maps (this does not count the partially
   # filled maps.
   maps_wide = (max_steps // width) - 1
   odd_maps = ((maps_wide // 2) * 2 + 1) ** 2
   even_maps = (((maps_wide + 1) // 2) * 2) ** 2
   print('traversal is ' + str(maps_wide) + ' maps wide')
   print('number of odd maps = ' + str(odd_maps))
   print('number of even maps = ' + str(even_maps))

   # Calculate the number of locations visited on fully
   # visited odd maps and fully visited even maps.
   # Then calculate the total.
   odd_locs_full = odd_maps * odd_fill
   even_locs_full = even_maps * even_fill
   print('odd_locations_full = ' + str(odd_locs_full))
   print('even_locations_full = ' + str(even_locs_full))
   total_full = odd_locs_full + even_locs_full
   print('total_locations_full = ' + str(total_full))

   # Now we need to deal with the partially filled maps.
   # We start with the four corner cases.
   top_locs = fillMap(area_map, (width - 1, start[1]), width - 1)           
   right_locs = fillMap(area_map, (start[0], 0), width - 1)
   bottom_locs = fillMap(area_map, (0, start[1]), width - 1)
   left_locs = fillMap(area_map, (start[0], width - 1), width - 1)
   four_corners = top_locs + right_locs + bottom_locs + left_locs
   print('top paritally filled locations = ' + str(top_locs))
   print('right paritally filled locations = ' + str(right_locs))
   print('bottom paritally filled locations = ' + str(bottom_locs))
   print('left paritally filled locations = ' + str(left_locs))
   print('sum of the partially filled four corners = ' + str(four_corners))

   # Now we deal with the remaining cases; those of
   # the top-right, bottom-right, bottom-left, and
   # top-left.  And each of these have two cases;
   # one in which the partial fill is small and
   # another in which the partial fill is large.
   tr_small = fillMap(area_map, (width - 1, 0), (width // 2) - 1) 
   br_small = fillMap(area_map, (0, 0), (width // 2) - 1) 
   bl_small = fillMap(area_map, (0, width - 1), (width // 2) - 1) 
   tl_small = fillMap(area_map, (width - 1, width - 1), (width // 2) - 1) 
   sum_small_segments = (maps_wide + 1) * (tr_small + br_small + bl_small + tl_small)

   tr_large = fillMap(area_map, (width - 1, 0), (width * 3 // 2) - 1)
   br_large = fillMap(area_map, (0, 0), (width * 3  // 2) - 1)
   bl_large = fillMap(area_map, (0, width - 1), (width * 3 // 2) - 1)
   tl_large = fillMap(area_map, (width - 1, width - 1), (width * 3 // 2) - 1)
   sum_large_segments = maps_wide * (tr_large + br_large + bl_large + tl_large)

   # Sum it all up for the total number of locations that can be reached.
   total_locs = total_full + four_corners + sum_small_segments + sum_large_segments
   print('total locations = ' + str(total_locs))
   
