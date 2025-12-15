# Scan through each game and determine the minimal
# number of stones of each color to be able to get
# the results shown within the game.

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
   values = readFile("input2a.txt")
   games = parseInput(values)

   # Create a list of the power values for each game.
   # The power value of a game is the product of 
   power = []
   
   # Iterate throught the games (data set).
   for g in games:
      # Initialize the minimum number of stones needed
      # to zero.
      minStones = { "red":0, "green":0, "blue":0 }

      # For each drawn set of stones, if the number
      # drawn if greater than the minStones of that
      # color, then update.
      for number, color in g:
         if number > minStones[color]:
            minStones[color] = number

      # Once the minimum number of stones are found,
      # multiply them together and store the result.
      power.append(minStones['red'] * minStones['green'] * minStones['blue'])

   # Display the sum of the powers.
   print('Sum of powers = ' + str(sum(power)))

   
        
    
        
