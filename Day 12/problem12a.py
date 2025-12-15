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


def countPossibles(state):
   state1, state2 = state
   # count unknown states in first representation
   s1_list = list(state1)
   count = s1_list.count('?')

   total_count = 0

   # use binary counting within loop
   max_iteration = pow(2, count)
   for i in range(max_iteration):
      bin_str = str(bin(i))[2:]
      while len(bin_str) < count:
         bin_str = '0' + bin_str

      # split current value based on original template
      mod_state = [ j for j in s1_list ]
      str_index = 0
      for j in range(len(mod_state)):
         if mod_state[j] == '?':
            if bin_str[str_index] == '0':
               mod_state[j] = '.'
            elif bin_str[str_index] == '1':
               mod_state[j] = '#'
            else:
               print('Error: unknown bin_str value: ' + bin_str[str_index])
            str_index += 1

      mod_state_str = ''.join(mod_state)
      #print(mod_state_str)
      
      # split based on empty slots
      mod_state_lst = mod_state_str.split('.')
   
      # count number of elements and compare with second representation
      mod_state_count = [ len(m) for m in mod_state_lst if len(m) > 0 ]
      if str(mod_state_count) == str(state2):
         total_count += 1

   return total_count
      

if __name__ == '__main__':
   lines = readFile("input12b.txt")
   states = parseInput(lines)
   count = 0
   check_num = 0
   for s in states:
      check_num += 1
      print('checking ' + str(check_num) + ' out of ' + str(len(states))) 
      local_count = countPossibles(s)
      print('local count = ' + str(local_count))
      count += local_count
      print('count = ' + str(count))
      print()
   print('possible arrangements = ' + str(count))
   
   
