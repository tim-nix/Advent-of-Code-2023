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
   return [ list(line) for line in lines ]


if __name__ == '__main__':
   lines = readFile("input16b.txt")
   cavern = parseInput(lines)
   beams = [ (0, -1) ]
   directions = [ 'east' ]
   activated = set()
   while len(beams) > 0:
      new_beams = []
      new_directions = []
      #print(beams)
      #print(directions)
      #print()
      for b_i in range(len(beams)):
         x, y = beams[b_i]
         direction = directions[b_i]
         if direction == 'east':
            if (y + 1) < len(cavern[x]):
               if (cavern[x][y + 1]) == '/':
                  if (x, y + 1, 'north') not in activated:
                     new_beams.append((x, y + 1))
                     new_directions.append('north')
                     activated.add((x, y + 1, 'north'))
               elif (cavern[x][y + 1]) == '\\':
                  if (x, y + 1, 'south') not in activated:
                     new_beams.append((x, y + 1))
                     new_directions.append('south')
                     activated.add((x, y + 1, 'south'))
               elif (cavern[x][y + 1]) == '|':
                  if (x, y + 1, 'north') not in activated:
                     new_beams.append((x, y + 1))
                     new_directions.append('north')
                     activated.add((x, y + 1, 'north'))
                  if (x, y + 1, 'south') not in activated:
                     new_beams.append((x, y + 1))
                     new_directions.append('south')
                     activated.add((x, y + 1, 'south'))
               else:
                  if (x, y + 1, direction) not in activated:
                     new_beams.append((x, y + 1))
                     new_directions.append(direction)
                     activated.add((x, y + 1, direction))
               

         elif direction == 'south':
            if (x + 1) < len(cavern):
               if (cavern[x + 1][y]) == '/':
                  if (x + 1, y, 'west') not in activated:
                     new_beams.append((x + 1, y))
                     new_directions.append('west')
                     activated.add((x + 1, y, 'west'))
               elif (cavern[x + 1][y]) == '\\':
                  if (x + 1, y, 'east') not in activated:
                     new_beams.append((x + 1, y))
                     new_directions.append('east')
                     activated.add((x + 1, y, 'east'))
               elif (cavern[x + 1][y]) == '-':
                  if (x + 1, y, 'west') not in activated:
                     new_beams.append((x + 1, y))
                     new_directions.append('west')
                     activated.add((x + 1, y, 'west'))
                  if (x + 1, y, 'east') not in activated:
                     new_beams.append((x + 1, y))
                     new_directions.append('east')
                     activated.add((x + 1, y, 'east'))
               else:
                  if (x + 1, y, direction) not in activated:
                     new_beams.append((x + 1, y))
                     new_directions.append(direction)
                     activated.add((x + 1, y, direction))


         elif direction == 'west':
            if (y - 1) >= 0:
               if (cavern[x][y - 1]) == '/':
                  if (x, y - 1, 'south') not in activated:
                     new_beams.append((x, y - 1))
                     new_directions.append('south')
                     activated.add((x, y - 1, 'south'))
               elif (cavern[x][y - 1]) == '\\':
                  if (x, y - 1, 'north') not in activated:
                     new_beams.append((x, y - 1))
                     new_directions.append('north')
                     activated.add((x, y - 1, 'north'))
               elif (cavern[x][y - 1]) == '|':
                  if (x, y - 1, 'north') not in activated:
                     new_beams.append((x, y - 1))
                     new_directions.append('north')
                     activated.add((x, y - 1, 'north'))
                  if (x, y - 1, 'south') not in activated:
                     new_beams.append((x, y - 1))
                     new_directions.append('south')
                     activated.add((x, y - 1, 'south'))
               else:
                  if (x, y - 1, direction) not in activated:
                     new_beams.append((x, y - 1))
                     new_directions.append(direction)
                     activated.add((x, y - 1, direction))
 
         elif direction == 'north':
            if (x - 1) >= 0:
               if (cavern[x - 1][y]) == '/':
                  if (x - 1, y, 'east') not in activated:
                     new_beams.append((x - 1, y))
                     new_directions.append('east')
                     activated.add((x - 1, y, 'east'))
               elif (cavern[x - 1][y]) == '\\':
                  if (x - 1, y, 'west') not in activated:
                     new_beams.append((x - 1, y))
                     new_directions.append('west')
                     activated.add((x - 1, y, 'west'))
               elif (cavern[x - 1][y]) == '-':
                  if (x - 1, y, 'west') not in activated:
                     new_beams.append((x - 1, y))
                     new_directions.append('west')
                     activated.add((x - 1, y, 'west'))
                  if (x - 1, y, 'east') not in activated:
                     new_beams.append((x - 1, y))
                     new_directions.append('east')
                     activated.add((x - 1, y, 'east'))
               else:
                  if (x - 1, y, direction) not in activated:
                     new_beams.append((x - 1, y))
                     new_directions.append(direction)
                     activated.add((x - 1, y, direction))

      beams = new_beams
      directions = new_directions

   tiles_activated = set()
   for val in activated:
      tiles_activated.add((val[0], val[1]))

   print('tiles activated = ' + str(len(tiles_activated)))
            
               
               
   
