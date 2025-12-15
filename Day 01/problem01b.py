# Only replace the spelled-out digit if it is necessary
# Otherwise, could affect other spelled-out digits.
# For example, "...eightwo..." could resolve to "...8wo..."
# or "...eigh2..." depending on the rest of the string.

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
   values = readFile("input1b.txt")

   # Create a mapping between the word representation
   # and the digit representation.
   mapping = { "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9" }

   values2 = []

   # For each string of input:
   for v in values:
      # Determine the index of the first digit within
      # the string.
      d_list = [ x.isdigit() for x in list(v) ]
      d_first = -1
      if True in d_list:
         d_first = d_list.index(True)


      # Determine the first (if any) location of a
      # word representation of a digit.
      v2 = v
      first = ""
      first_loc = -1
      for m in mapping.keys():
         loc = v2.find(m)
         if (loc != -1) and ((first_loc == -1) or (loc < first_loc)):
            first = m
            first_loc = loc

      #print('found ' + first + ' at position ' + str(first_loc))

      # Determine which occurs first: the digit or
      # the word. If the word, then replace it with
      # a digit.
      if (first_loc != -1) and ((d_first == -1) or (first_loc < d_first)):
         v2 = v2.replace(first, mapping[first], 1)

      # Determine the index of the last digit within
      # the string.
      d_list = [ x.isdigit() for x in list(v2) ]
      d_last = -1
      while True in d_list:
         i = d_list.index(True)
         d_last = i
         d_list[i] = False

      #print('last digit: ' + str(d_last))

      # Determine the last (if any) location of a
      # word representation of a digit.
      last = ""
      last_loc = -1
      for m in mapping.keys():
         loc = v2.rfind(m)
         if (loc != -1) and ((last_loc == -1) or (loc > last_loc)):
            last = m
            last_loc = loc

      #print('found ' + last + ' at position ' + str(last_loc))

      # Determine which occurs last: the digit or
      # the word. If the word, then replace it with
      # a digit.
      if (last_loc != -1) and (last_loc > d_last):
         v2 = v2.replace(last, mapping[last])
            
      values2.append(v2)

   # With the modified string, process it the same
   # as was done in part a.
   calibrations = list()
   for v in values2:
      c = [ x for x in list(v) if x.isdigit() ]
      calibrations.append(int(c[0] + c[-1]))

   #for i in range(len(values)):
   #   print(values[i] + "   " + values2[i] + "   " + str(calibrations[i]))
      
   print('answer = ' +str(sum(calibrations)))
   
        
    
        
