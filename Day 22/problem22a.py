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
   bricks = []
   for line in lines:
      first_loc, second_loc = line.split('~')
      first_coords = [ int(x) for x in first_loc.split(',') ]
      second_coords = [ int(x) for x in second_loc.split(',') ]

      bricks.append(first_coords + second_coords)

   bricks.sort(key=lambda a: a[2])
   
   return bricks


# Determine if the two bricks overlap in the x
# and y dimensions (ignores the z dimension).
def isOverlap(brick1, brick2):
   x_overlap = max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3])
   y_overlap = max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])

   return x_overlap and y_overlap


# Repeatedly iterate through the bricks and see
# if a given brick can be moved down by one z
# coordinate. Need to check to see if moving the
# brick will result in an overlap.  If not, then
# move the brick.
def applyGravity(bricks):
   for b_i, brick in enumerate(bricks):
      # if the brick is on the ground, move on
      if brick[2] - 1 == 0:
         continue
      
      # compare with all other bricks
      new_z = 1
      for brick2 in bricks[:b_i]:
         # if overlap, move on, otherwise, move brick
         if isOverlap(brick, brick2):
            if (brick2[5] + 1) > new_z:
               new_z = brick2[5] + 1

      brick[5] -= brick[2] - new_z
      brick[2] = new_z

   bricks.sort(key=lambda a: a[2])


# Determine if brick1 supports brick2; that is if
# brick2 is on top of and overlaps brick1.
def isSupport(brick1, brick2):
   # brick2 should be on top of brick1 and 
   # supported by brick1
   if (brick2[2] == brick1[5] + 1) and isOverlap(brick1, brick2):
      return True
   else:
      return False


# Count the number of removable bricks. To do this
# two dictionaries are generated: the first dictionary
# stores the set of bricks that each brick supports.
# The second dictionary stores the set of bricks
# that each brick is supported by.  These are then
# used to determine, for each brick, if the supported
# bricks are supported by other bricks.
def countRemovable(bricks):
   # generate dictionaries of sets that each brick
   # supports and that each brick is supported by.
   supports = dict()
   supported = dict()
   for index in range(len(bricks)):
      supports[index] = set()
      supported[index] = set()

   for index1, brick1 in enumerate(bricks):
      for index2, brick2 in enumerate(bricks):
         if isSupport(brick1, brick2):
            supports[index1].add(index2)  
            supported[index2].add(index1)

   # For each brick, pull out the bricks it supports
   # and see if they are each supported by another
   # brick. If so, then it is removable, so count it.
   count = 0
   for index, brick in enumerate(bricks):
      canRemove = True
      for s in supports[index]:
         if len(supported[s]) == 1:
            canRemove = False
      if canRemove:
         count += 1

   return count


if __name__ == '__main__':
   # Read in the file and organize the data
   lines = readFile("input22b.txt")
   bricks = parseInput(lines)
   
   # Modify the data set so that each brick
   # settles as low as it is able.
   applyGravity(bricks)

   # Count the number of removable bricks
   count = countRemovable(bricks)
   print('count = ' + str(count))
   
   
