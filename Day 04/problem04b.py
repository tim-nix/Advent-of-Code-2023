# Iterate through the collection of cards. For each
# card, calculate the number of matchs (as was done
# in part A.  However, the number of matches results
# in that many subsequent cards being copied. So,
# use a list of values (initialized to 1 for each
# card) identifying how many of each card is owned.

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


if __name__ == '__main__':
   lines = readFile("input4b.txt")

   # Make a list of the number of cards of each
   # type possessed (1 for each card).
   cards = [ 1 for i in range(len(lines)) ]
   for card in range(len(cards)):
      # Eliminate header.
      card2 = lines[card].split(':')
      
      # Split into winning numbers and numbers.
      card3 = card2[1].split('|')
      winning = card3[0].split()
      numbers = card3[1].split()
      
      # Turn each into a set.
      win_set = set(winning)
      num_set = set(numbers)
      
      # Determine size of intersection of the two sets.
      matches = len(win_set.intersection(num_set))

      # Copy the number of cards following the current
      # 'winning' card equal to the number of matches
      # and add them to the collection of cards.
      if matches > 0:
         for i in range(card + 1, card + matches + 1):
            if i <= len(cards):
               cards[i] += cards[card]
            else:
               print("Error: no matching card")


   # Calculate the number of cards possessed and print
   # the result.
   print('sum = ' + str(sum(cards)))
        
