import time
import sympy

   
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

   
if __name__ == '__main__':
   start_time = time.time()
   # Read in the file and organize the data
   lines = readFile("input24b.txt")
   hailstones = parseInput(lines)

   # x_r, y_r, z_r are the initial rock coordinates.
   # dx_r, dy_r, dz_r is the rock velocity.
   # x_i, y_i, z_i are the coordinates for each hailstone i.
   # dx_i, dy_i, dz_i are the velocities for each hailstone i.

   # When the rock intercepts with each hailstone at time t_i:
   # x_r + t_i * dx_r = x_i + t_i * dx_i
   # y_r + t_i * dy_r = y_i + t_i * dy_i
   # z_r + t_i * dz_r = z_i + t_i * dz_i

   # Solve to t_i for hailstone i:
   # t_i = (x_i - x_r) / (dx_r - dx_i)
   # t_i = (y_i - y_r) / (dy_r - dy_i)
   # t_i = (z_i - z_r) / (dz_r - dz_i)

   # At time t_i, the following equalities hold:
   # (x_i - x_r) / (dx_r - dx_i) = (y_i - y_r) / (dy_r - dy_i)
   # (y_i - y_r) / (dy_r - dy_i) = (z_i - z_r) / (dz_r - dz_i)
   # (x_i - x_r) / (dx_r - dx_i) = (z_i - z_r) / (dz_r - dz_i)

   # Use sympy to solve system of equations
   # Add solution labels.
   x_r, y_r, z_r, dx_r, dy_r, dz_r = sympy.symbols('x_r y_r z_r dx_r dy_r dz_r', integer = True)
   
   # Add equations
   equations = []
   for x_i, y_i, z_i, dx_i, dy_i, dz_i in hailstones[:10]:
      equations.append((x_r - x_i) * (dy_i - dy_r) - (y_r - y_i) * (dx_i - dx_r))
      equations.append((y_r - y_i) * (dz_i - dz_r) - (z_r - z_i) * (dy_i - dy_r))
      equations.append((z_r - z_i) * (dx_i - dx_r) - (x_r - x_i) * (dz_i - dz_r))

   # Solve equations
   answers = sympy.solve(equations)

   # Print results
   answer = (answers[0][x_r], answers[0][y_r], answers[0][z_r], answers[0][dx_r], answers[0][dy_r], answers[0][dz_r])
   print('starting location = ' + str(answer))
   print('sum = ' + str(answer[0] + answer[1] + answer[2]))
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
