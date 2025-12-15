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
   return lines[0].split(',')


def calcHash(string):
   current = 0
   for s in string:
      a_val = ord(s)
      current += a_val
      current = (current * 17) % 256

   return current


if __name__ == '__main__':
   lines = readFile("input15b.txt")
   strings = parseInput(lines)
   sum = 0
   for s in strings:
      sum += calcHash(s)
   print('sum = ' + str(sum))
