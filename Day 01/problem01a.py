# This solution parses the input, extracts the digits
# and appends them together into a string which is
# then converted into an integer.  The integer is
# added to a list and, once all data is converted, the
# sum is calculated.

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
   calibrations = []
   # For each line of input, find the two digits.
   for v in values:
      c = [ x for x in list(v) if x.isdigit() ]
      # Convert the two digit string into and integer.
      calibrations.append(int(c[0] + c[-1]))

   # Calculate the sum of the two-digit numbers
   print(sum(calibrations))
   
        
    
        
