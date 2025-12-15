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
   boxes = [ [] for i in range(256) ]
   for s in strings:
      if '=' in s:
         s_lst = s.split('=')
         box_i = calcHash(s_lst[0])
         lens_i = -1
         replaced = False
         for lens_i in range(len(boxes[box_i])):
            if s_lst[0] == boxes[box_i][lens_i][0]:
               boxes[box_i][lens_i] = (s_lst[0], s_lst[1])
               replaced = True
         if not replaced:
            boxes[box_i].append((s_lst[0], s_lst[1]))
      elif '-' in s:
         lens = s[:-1]
         box_i = calcHash(lens)
         lens_i = -1
         for lens_i in range(len(boxes[box_i])):
            if lens == boxes[box_i][lens_i][0]:
               boxes[box_i].pop(lens_i)
               break
      else:
         print('Error: unknown string s = ' + s)

   calc_power = 0
   for i in range(len(boxes)):
      for j in range(len(boxes[i])):
         power = (i + 1) * int(boxes[i][j][1]) * (j + 1)
         #print(power)
         calc_power += power

   print('total power = ' + str(calc_power))
