# Convert the input into a single time value and a
# single distance value by removing whitespace
# between digits within the same line. Then, as
# before, determine how many ways there are to
# hold the button for some amount of time, so that
# when released, the boat will travel farther than
# the specified distance.
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

# The file input consists of two lines of text
# that actually only represent the time and (goal)
# distance of a single race. However, the time and
# distance is broken up by spaces. Convert each
# line into a single integer by ignoring spaces, and
# pair up the first line (time) with the second line
# (the corresponding distance goal) as a tuple and
# return the tuple.
def parseInput(lines):
   time = lines[0].split(':')
   distance = lines[1].split(':')

   time = time[1].replace(" ", "")
   distance = distance[1].replace(" ", "")

   results = (int(time), int(distance))
   
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
   r_time, goal = parseInput(lines)

   # For the time, distance goal pair, determine the
   # number of ways to win by holding down the button
   # for all integer lengths of times from zero to
   # time - 1.
   wins = [ calcDistance(i, r_time) > goal for i in range(r_time) ]
   output = wins.count(True)

   # Display the results.
   print('output = ' + str(output))

   print("\n\n--- %s seconds ---" % (time.time() - start_time))
   
