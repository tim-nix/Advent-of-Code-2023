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
   converted = []
   for line in lines:
      numbers = [ int(i) for i in line.split() ]
      converted.append(numbers)

   return converted


def genDiffs(start):
   diffs = [ start[-1] ]
   done = False
   array = [ i for i in start ]
   # print(array)
   while not done:
      new_array = [ array[i + 1] - array[i] for i in range(len(array) - 1) ]
      done = True
      for j in new_array:
         if j != 0:
            done = False
            break
      diffs.append(new_array[-1])
      array = new_array
      # print(array)
      
   return diffs
            

if __name__ == '__main__':
   lines = readFile("input9b.txt")
   history = parseInput(lines)
   sum_values = 0
   progress = 1
   for start in history:
      print(str(progress) + ' of ' + str(len(history)))
      progress += 1
      diffs = genDiffs(start)
      diffs.reverse()
      value = sum(diffs)
      sum_values += value

   print('sum of values = ' + str(sum_values))

   
   
