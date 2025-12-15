# Iterate through each line of text looking for digits.
# If a number is found, look for an adjacent symbol.
# If the symbol is found, add the number to the sum.

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
   lines = readFile("input3b.txt")

   # Create a list of found numbers within each line
   # of input.
   foundNumbers = []
   for index in range(len(lines)):
      line = lines[index]
      done = False
      first = 0
      last = 0
      while not done:
         # Find first digit
         while (first < len(line)) and (not line[first].isdigit()):
            first += 1
            
         if first >= len(line):
            done = True
         else:
            # Find last digit
            last = first
            while (last < len(line)) and (line[last].isdigit()):
               last += 1
               
            # Once a number is found, look all around for a symbol
            nearSymbol = False
            for i in range(index - 1, index + 2):
               for j in range(first - 1, last + 1):
                  if (i >= 0) and (i < len(lines)) and (j >= 0) and (j < len(line)):
                     if (not lines[i][j].isdigit()) and (lines[i][j] != '.'):
                        nearSymbol = True

            # If symbol found, pull out number and add to list
            if nearSymbol:
               number = ''
               for i in range(first, last):
                  number += line[i]
               foundNumbers.append(int(number))
               
            # Continue until end of line is reached
            first = last + 1

   # Print out the sum of the found numbers with a symbol adjacent
   # to it.
   print('sum = ' + str(sum(foundNumbers)))

   
   
        
    
        
