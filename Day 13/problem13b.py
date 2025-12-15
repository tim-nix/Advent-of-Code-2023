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


def rotatePattern(pattern):
   rot_pattern = []
   for j in range(len(p[0])):
      new_row = []
      for i in range(len(p) - 1, -1, -1):
         new_row.append(p[i][j])
      rot_pattern.append(''.join(new_row))

   return rot_pattern


def getReflectionLine(row1, row2, check_p):
   for row in range(row1, len(check_p) - 1):
      # find two rows that are identical,
      if (check_p[row] == check_p[row + 1]) and (row >= row1) and (row <= row2):
         #print('match at row ' + str(row) + ' and row ' + str(row + 1))
         # then look for symmetry
         symmetry = True
         #print('minimum of ' + str(row) + ' and ' + str(len(check_p) - row - 2))
         min_range = min(row, len(check_p) - row - 2)
         if (row1 >= row - min_range) and (row2 <= row + 1 + min_range): 
            for i in range(min_range + 1):
               #print(i)
               if check_p[row - i] != check_p[row + 1 + i]:
                  #print('row ' + str(row - i) + ' does not match row ' + str(row + 1 + i))
                  symmetry = False
            if symmetry:
               #print('match: appending row ' + str(row + 1))
               return row + 1

   return -1

   
if __name__ == '__main__':
   lines = readFile("input13b.txt")
   patterns = parseInput(lines)
   row_symmetry = []
   col_symmetry = []

   check_list = [ 0, 59, 93 ]

   # for each pattern, find row reflection
   for p_index in range(len(patterns)):
      p = patterns[p_index]
      smudge_found = False
      
      check_p = p
      #print('next pattern')
      #for line in p:
      #   print(line)
      #print()
      #print('len(check_p) = ' + str(len(check_p)))
      for row1 in range(len(check_p) - 1):
         # find two rows that are one off from each other
         for row2 in range(row1 + 1, len(check_p)):
            diffs = 0
            #print('comparing ' + str(row1) + ' and ' + str(row2))
            for i in range(len(check_p[row1])):
               if check_p[row1][i] != check_p[row2][i]:
                  diffs += 1
            #print('found ' + str(diffs) + ' differences')
            
            if (diffs == 1):
               #print('testing modified map on row ' + str(row1) + ' and row ' + str(row2))
               # make change and test it
               old_row = check_p[row1]
               check_p[row1] = check_p[row2]

               found_i = getReflectionLine(row1, row2, check_p)
               if (found_i > 0) and ((p_index, found_i) not in row_symmetry):
                  smudge_found = True
                  row_symmetry.append((p_index, found_i))
                  
               check_p[row1] = old_row

      if not smudge_found:
         # rotate pattern by 90 degrees
         rot_pattern = rotatePattern(p)
         check_p = rot_pattern
         #for line in rot_pattern:
         #   print(line)

         #print('next pattern')
         for row1 in range(len(check_p) - 1):
            
            # find two rows that are one off from each other
            for row2 in range(row1 + 1, len(check_p)):
               diffs = 0
               #print('comparing ' + str(row1) + ' and ' + str(row2))
               for i in range(len(check_p[row1])):
                  if check_p[row1][i] != check_p[row2][i]:
                     diffs += 1
               #print('found ' + str(diffs) + ' differences')
               
               if (diffs == 1):
                  #print('testing modified map on row ' + str(row1) + ' and row ' + str(row2))
                  # make change and test it
                  old_row = check_p[row1]
                  check_p[row1] = check_p[row2]

                  #print('made change')
                  #for line in check_p:
                  #   print(line)
                  #print()

                  found_i = getReflectionLine(row1, row2, check_p)
                  if (found_i > 0) and ((p_index, found_i) not in col_symmetry):
                     col_symmetry.append((p_index, found_i))
                     
                  check_p[row1] = old_row
                  
   # calculate score
   total = row_symmetry + col_symmetry
   total.sort()
   print(total)
   score = 0
   for s in row_symmetry:
      score += 100 * s[1]
   for s in col_symmetry:
      score += s[1]

   print('43222 is too high')
   print('41522 is not correct')
   print('score = ' + str(score))
   print()


   
   
   
