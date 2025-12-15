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
   patterns = []
   next_pattern = []
   for line in lines:
      if line == '':
         patterns.append(next_pattern)
         next_pattern = []
      else:
         next_pattern.append(line)
   patterns.append(next_pattern)

   return patterns

   
if __name__ == '__main__':
   lines = readFile("input13b.txt")
   patterns = parseInput(lines)
   row_symmetry = []
   col_symmetry = []
   
   # for each pattern, find row reflection
   for p in patterns:
      print('\nnext pattern')
      for row in range(len(p) - 1):
         # find two rows that are identical,
         if p[row] == p[row + 1]:
            #print('match at row ' + str(row) + ' and row ' + str(row + 1))
            # then look for symmetry
            symmetry = True
            #print('minimum of ' + str(row) + ' and ' + str(len(p) - row - 2))
            min_range = min(row, len(p) - row - 2)
            for i in range(min_range + 1):
               print(i)
               if p[row - i] != p[row + 1 + i]:
                  symmetry = False
            if symmetry:
               print('match; appending row ' + str(row + 1))
               row_symmetry.append(row + 1)
            else:
               print('no match')

      for line in p:
         print(line)
      print()

      # rotate pattern by 90 degrees
      rot_pattern = []
      for j in range(len(p[0])):
         new_row = []
         for i in range(len(p) - 1, -1, -1):
            new_row.append(p[i][j])
         rot_pattern.append(''.join(new_row))

      for line in rot_pattern:
         print(line)

      #print('next pattern')
      for row in range(len(rot_pattern) - 1):
         # find two rows that are identical,
         if rot_pattern[row] == rot_pattern[row + 1]:
            print('match at row ' + str(row) + ' and row ' + str(row + 1))
            # then look for symmetry
            symmetry = True
            print('minimum of ' + str(row) + ' and ' + str(len(rot_pattern) - row - 2))
            min_range = min(row, len(rot_pattern) - row - 2)
            for i in range(min_range + 1):
               print(i)
               if rot_pattern[row - i] != rot_pattern[row + 1 + i]:
                  symmetry = False
            if symmetry:
               print('match; appending column ' + str(row + 1))
               col_symmetry.append(row + 1)
            else:
               print('no match')

   # calculate score
   print('row matches = ' + str(row_symmetry))
   print('col matches = ' + str(col_symmetry))
   score = 0
   for s in row_symmetry:
      score += 100 * s
   for s in col_symmetry:
      score += s

   print('score = ' + str(score))
   
   
   
