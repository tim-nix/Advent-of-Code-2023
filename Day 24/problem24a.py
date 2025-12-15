import math

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


# Convert each line into a tuple of six integer values.
def parseInput(lines):
   new_lines = []
   for i in range(len(lines)):
      lines[i] = lines[i].replace(' ', '')
      lines[i] = lines[i].replace('@', ',')
      new_lines.append([ int(a) for a in lines[i].split(',') ])

   return new_lines


# Determine if two lines will intersect in the x, y plane.
def willIntersect(line1, line2, minVal, maxVal):
   # Calculate the slope of both lines.
   m1 = line1[4] / line1[3]
   m2 = line2[4] / line2[3]

   # If the two lines are parallel, they will never intersect.
   if m1 == m2:
      return False

   # Calculate the y intercept for both lines.
   b1 = line1[1] - (m1 * line1[0])
   b2 = line2[1] - (m2 * line2[0])

   # Calculate the x coordinate where the lines intersect.
   x_i = (b2 - b1) / (m1 - m2)

   # If the intersect occurred in the past then return False.
   if (((x_i - line1[0]) / line1[3]) < 0) or (((x_i - line2[0]) / line2[3]) < 0):
      return False

   # If the intersect occurs outside of the specified range
   # then return False.
   if (x_i < minVal) or (x_i > maxVal):
      return False
   

   # Calculate the y coordinate where the lines intersect.
   y_i = ((b1 / m1) - (b2 / m2)) / ((1 / m1) - (1 / m2))

   # If the intersect occurred in the past then return False.
   if (((y_i - line1[1]) / line1[4]) < 0) or (((y_i - line2[1]) / line2[4]) < 0):
      return False

   # If the intersect occurs outside of the specified range
   # then return False.
   if (y_i < minVal) or (y_i > maxVal):
      return False

   # The lines intersect in the future, within the specified
   # bounds.
   return True

   
if __name__ == '__main__':
   # Read in the file and organize the data.
   lines = readFile("input24b.txt")
   lines = parseInput(lines)

   # The intersections must occur within this interval.
   minVal = 200000000000000
   maxVal = 400000000000000

   # Count how many lines intersect within the interval
   # (and in the future).
   count = 0
   for i in range(len(lines) - 1):
      for j in range(i + 1, len(lines)):
         if willIntersect(lines[i], lines[j], minVal, maxVal):
            count += 1

   # Print the result.
   print('count = ' + str(count))
         

   
   
   
   
   
