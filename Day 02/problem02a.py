# This solution looks at each game.  Within each game, the
# number of drawn stones (in a single draw) is compared
# with the maximum number of stones.  If the number drawn
# is greater than the maximum number of stones, then the
# game is not possible and is invalid.

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


# Parse each game string and convert it into a list of
# tuples; each tuple corresponds to a value (the number
# of stones seen) and the color of the stones.
def parseInput(values):
   results = []
   for v in values:
      # First, get rid of the game id header; we will
      # recognize different games by different lists.
      p1 = v.split(':')
      
      # Next, break up the game into each 'showing'.
      # Each game is a list with each draw being a tuple
      # with the number of stones drawn and the color
      # of those stones.
      p2 = p1[1].split(';')
      game = []
      for p3 in p2:
         p4 = p3.split(',')
         showings = []
         for p5 in p4:
            p6 = p5.strip()
            p7 = p6.split(' ')
            game.append((int(p7[0]), p7[1]))

      # Add the game to the list of games.
      results.append(game)

   return results

if __name__ == '__main__':
   values = readFile("input2b.txt")
   games = parseInput(values)
   
   # Define the maximum number of stones for each color.
   maxStones = { "red":12, "green":13, "blue":14 }

   # Create a list of Boolean values; True is the game is
   # possible and False otherwise.
   valids = []

   # Iterate throught the games (data set). The game id
   # corresponds to the index in the list of games (and
   # the list of valids).
   for g in games:
      valid = True
      # Iterate through the drawn stones (the tuples
      # within the list).
      for number, color in g:
         # If the number of drawn stones is greater than
         # the maximum number of stones for that color.
         if number > maxStones[color]:
            valid = False
            break

      # Add the validity of the game to the list of valids
      valids.append(valid)
      
   # Sum the games that are invalid; that is, the indices of
   # the False values within the valid list.
   sum = 0
   for v in range(len(valids)):
      if valids[v]:
         sum += v + 1

   # Print out the results.
   print('sum = ' + str(sum))
   
        
    
        
