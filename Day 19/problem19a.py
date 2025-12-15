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
   index = lines.index('')
   workflow = lines[:index]
   ratings_str = lines[index + 1:]

   # Turn the strings for each workflow into a dictionary
   # entry.  The key is the name of the workflow (e.g., 'in')
   # and the value is a tuple of rules.
   # A normal rule (with a comparator) will be a 4-tuple, e.g.,
   # ('x', '>', 1234, 'xgf') with the third value as an
   # integer and all other values as strings.
   workflow_dict = dict()
   for w in workflow:
      instruct = w.split('{')
      name = instruct[0]
      checks = instruct[1][:-1].split(',')
      for c_i in range(len(checks)):
         if ':' in checks[c_i]:
            compare, next_step = checks[c_i].split(':')
            var = compare[0]
            operator = compare[1]
            value = int(compare[2:])
            checks[c_i] = (var, operator, value, next_step)
      
      workflow_dict[name] = checks

   # Turn the string containing the variable values 'xmas'
   # into a tuple of values (x, m, a, s).
   ratings = []
   for r in ratings_str:
      # chop off the surrounding curly braces and
      # split string into list by commas
      r_lst = r[1:-1].split(',')
      
      # convert it into tuple of integers
      xmas_lst = []
      for xmas in r_lst:
         xmas_lst.append(int(xmas.split('=')[1]))
      ratings.append(tuple(xmas_lst))
      
   return (workflow_dict, ratings)

      
if __name__ == '__main__':
   lines = readFile("input19b.txt")
   workflow, ratings = parseInput(lines)
   var = dict()
   sum_accepted = 0

   # Iterate through the ratings.
   for r in ratings:
      # for easy reference, turn the ratings tuple
      # into a dictionary
      var['x'] = r[0]
      var['m'] = r[1]
      var['a'] = r[2]
      var['s'] = r[3]

      # The initial state is always 'in'
      current = 'in'
      
      # Apply rules until the rating leads to an
      # accept 'A' or reject 'R'.
      while (current != 'A') and (current != 'R'):
         # Given the current workflow, iterate through
         # the rules.
         for rule in workflow[current]:
            # In this case, none of the previous rules
            # evaluated to true, so change the state to
            # this value
            if type(rule) == str:
               current = rule
               break
            # In this case, the variable (rule[0]) is
            # evaluated to determine if it is larger
            # than the value (rule[2]).  If so, then
            # the new state becomes rule[3].            
            elif rule[1] == '>':
               if var[rule[0]] > rule[2]:
                  current = rule[3]
                  break
            # In this case, the variable (rule[0]) is
            # evaluated to determine if it is smaller
            # than the value (rule[2]).  If so, then
            # the new state becomes rule[3].
            elif rule[1] == '<':
               if var[rule[0]] < rule[2]:
                  current = rule[3]
                  break

      # if the current state is an accept state, then
      # add the sum of the variables 'xmas' to the
      # running total.
      if current == 'A':
         sum_accepted += sum(r)

   # print out the running total sum of all ratings that
   # were accepted.
   print('sum of accepted ratings = ' + str(sum_accepted))
   
   
