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
   parsed = []
   for line in lines:
      p_line = line.split()
      state1 = p_line[0]
      state2 = p_line[1]
      state2 = state2.split(',')
      state2 = [ int(state) for state in state2 ]
      parsed.append((state1, state2))

   return parsed


def expandState(state):
   state1, state2 = state
   state1 = state1 + (('?' + state1) * 4)
   state2 = state2 * 5

   state1a = ''
   dots = False
   for s in state1:
      if s == '.' and not dots:
         dots = True
         state1a += s
      elif s != '.':
         dots = False
         state1a += s

   return (state1a, state2)

def countPossibles(state):
   def recursiveCount(current, state, matching):
      #print()
      #print('current = ' + current)
      #print('state = ' + state)
      #print('matching = ' + matching)
      if ('#' not in state) and (matching == ''):
         #print('Yes: good match')
         return 1
      
      if (state == '') or (matching == ''):
         #print('Nope: reached the end, but no match')
         return 0

      if ('#' in state) and (matching == ''):
         #print('Nope: still some state, but nothing to match with')
         return 0
      
      if len(state) < len(matching):
         #print('Nope: not enough state left')
         return 0

      if (state, matching) in solutions:
         #print('Found stored solution: solutions[' + str((state, matching)) + '] = ' + str(solutions[(state, matching)]))
         return solutions[(state, matching)]

      if state[0] == '#':
         if matching[0] == '#':
            count = recursiveCount(current + '#', state[1:], matching[1:])
            solutions[(state, matching)] = count
            return count
         else:
            return 0
      if (state[0] == '.') and (len(current) == 0):
         count = recursiveCount(current, state[1:], matching)
         solutions[(state, matching)] = count
         return count

      if (state[0] == '.') and (current[-1] == '.'):
         count = recursiveCount(current, state[1:], matching)
         solutions[(state, matching)] = count
         return count

      if (state[0] == '.') and (current[-1] != '.'):
         if matching[0] == '.':
            count = recursiveCount(current + '.', state[1:], matching[1:])
            solutions[(state, matching)] = count
            return count
         else:
            return 0

      if (state[0] == '?') and (len(current) == 0):
         count1 = recursiveCount(current, state[1:], matching)
         count2 = recursiveCount(current + '#', state[1:], matching[1:])
         solutions[(state, matching)] = count1 + count2
         return count1 + count2

      if (state[0] == '?') and (current[-1] == '.'):
         count1 = recursiveCount(current, state[1:], matching)
         count2 = recursiveCount(current + '#', state[1:], matching[1:])
            
         solutions[(state, matching)] = count1 + count2
         return count1 + count2

      if (state[0] == '?') and (current[-1] != '.'):
         count1 = 0
         if matching[0] == '.':
            count1 = recursiveCount(current + '.', state[1:], matching[1:])

         count2 = 0
         if matching[0] == '#':
            count2 = recursiveCount(current + '#', state[1:], matching[1:])

         solutions[(state, matching)] = count1 + count2
         return count1 + count2
      
      print('Error: unknown state')

   solutions = dict()
   state, lengths = state
   matching = ''
   for l in lengths:
      matching += l * '#'
      matching += '.'
   matching = matching[:-1]
   
   if state[0] == '.':
      return recursiveCount('', state[1:], matching)
   elif state[0] == '#':
      return recursiveCount('#', state[1:], matching[1:])
   elif state[0] == '?':
      count1 = recursiveCount('', state[1:], matching)
      count2 = recursiveCount('#', state[1:], matching[1:])
      return count1 + count2
      

if __name__ == '__main__':
   lines = readFile("input12b.txt")
   states = parseInput(lines)
   count = 0
   check_num = 0
   for s in states:
      check_num += 1
      #print('checking ' + str(check_num) + ' out of ' + str(len(states)))
      e_state = expandState(s)
      #e_state = s
      local_count = countPossibles(e_state)
      #print('count = ' + str(local_count))
      count += local_count
      
   print('possible arrangements = ' + str(count))
   
   
