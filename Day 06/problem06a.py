# For each race (time, distance), determine how many
# ways there are to hold the button for some amount
# of time, so that when released, the boat will
# travel farther than the specified distance. Multiply
# the number of ways for each race together.

import time

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



# The file input consists of two lines of text:
# a line of times and a line of (goal) distances.
# Convert each line into a list of integers, and
# pair up each time with its corresponding distance
# (as a tuple), returning a list of the tuples.
def parseInput(lines):
   times = lines[0].split(':')
   distances = lines[1].split(':')

   times = times[1].split()
   distances = distances[1].split()

   results = [ (int(times[i]), int(distances[i])) for i in range(len(times)) ]

   return results


# Calculate the distance traveled as the product
# of the run time (time after the button is released)
# and the length of time that the buttone is held.
def calcDistance(b_time, t_time):
   run_time = t_time - b_time
   distance = run_time * b_time

   return distance


if __name__ == '__main__':
   start_time = time.time()
   lines = readFile("input6b.txt")
   results = parseInput(lines)

   # For each time, distance goal pair, determine the
   # number of ways to win by holding down the button
   # for all integer lengths of times from zero to
   # time - 1.
   output = 1
   for r_time, goal in results:
      wins = [ calcDistance(i, r_time) > goal for i in range(r_time) ]
      # Multiply these numbers together to determine the
      # desired output.
      output *= wins.count(True)

   # Display the results.
   print('output = ' + str(output))

   print("\n\n--- %s seconds ---" % (time.time() - start_time))
   
