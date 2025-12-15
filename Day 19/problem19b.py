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

# The purpose of this function is to ensure that the
# min value for each variable is less than or equal to
# the max value for each variable.
#
# ranges = (x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max)
def checkRanges(ranges):
   for i in range(0, len(ranges) - 1, 2):
      if ranges[i + 1] <= ranges[i]:
         return False

   return True



# The purpose of this method is to recursively calculate
# the number of possible values that lead to an accept.
def findRangeCount(ranges, current, workflow):
   # If the current state is 'A', then calculate the
   # number of legal combinations based on the given
   # range.
   if current == 'A':
      combos = 1
      for i in range(0, len(ranges) - 1, 2):
         combos *= ranges[i + 1] - ranges[i] + 1
      return combos

   # If the current state is 'R', then the given range
   # lead to reject, and so lead to zero accept states.
   elif current == 'R':
      return 0

   # Otherwise, for the given state, apply each rule and
   # generate the appropriate range that leads to the next
   # state.
   to_add = 0
   total = 0
   for rule in workflow[current]:
      # In this case, the range should reflect that the
      # previous rules did not apply.  So, recurse on the
      # given range and the state specified by the rule
      # (even if rule is 'A' or 'R', recurse and let the
      # next function call handle it.
      if type(rule) == str:
         #print('recursive call')
         to_add = findRangeCount(ranges, rule, workflow)

      # In the next two cases, we modify the given ranges so
      # that this rule would evaluate to true and recursively
      # call the funcion on the new range and state.  But, 
      # we also need to determine the range of values that
      # would lead to this rule evaluating to false to be
      # applied to the next rule (if it exists).
      elif rule[1] == '>':
         #print('comparator >')
         if rule[0] == 'x':
            good_ranges = (rule[2] + 1, ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7]) 
            bad_ranges = (ranges[0], rule[2], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'm':
            good_ranges = (ranges[0], ranges[1], rule[2] + 1, ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], rule[2], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'a':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], rule[2] + 1, ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], rule[2], ranges[6], ranges[7])
         elif rule[0] == 's':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], rule[2] + 1, ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], rule[2])

         # The recursive call is only made if the ranges are legitimate.
         if checkRanges(good_ranges):
            to_add = findRangeCount(good_ranges, rule[3], workflow)

      elif rule[1] == '<':
         #print('comparator <')
         if rule[0] == 'x':
            good_ranges = (ranges[0], rule[2] - 1, ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (rule[2], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'm':
            good_ranges = (ranges[0], ranges[1], ranges[2], rule[2] - 1, ranges[4], ranges[5], ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], rule[2], ranges[3], ranges[4], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 'a':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], rule[2] - 1, ranges[6], ranges[7])
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], rule[2], ranges[5], ranges[6], ranges[7])
         elif rule[0] == 's':
            good_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], ranges[6], rule[2] - 1)
            bad_ranges = (ranges[0], ranges[1], ranges[2], ranges[3], ranges[4], ranges[5], rule[2], ranges[7])

         # The recursive call is only made if the ranges are legitimate.
         if checkRanges(good_ranges):
            to_add = findRangeCount(good_ranges, rule[3], workflow)

      # If the modified ranges (resulting from the rule evaluating to false)
      # are legitimate, then set them to ranges for the next rule.
      if checkRanges(bad_ranges):
         ranges = bad_ranges
      else:
         break

      # Add the number of combinations that lead to 'A' for
      # this rule to the total.
      total += to_add

   return total


if __name__ == '__main__':
   lines = readFile("input19b.txt")
   workflow, ratings = parseInput(lines)
   ranges = (1, 4000, 1, 4000, 1, 4000, 1, 4000)
   accepted = findRangeCount(ranges, 'in', workflow)
   print('accepted = ' + str(accepted))
   
   
