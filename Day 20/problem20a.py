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


# Parse the input into a dictionary of modules.  Each
# module will be indexed by name.  The value will be a
# tuple.  If the module is a conjunction or a flip-flop
# then the first element will be '%' or '&' as the
# indicator.  For all modules, the second element is
# a tuple of output modules; that is, the modules to
# which the current module sends pulses.  If the module
# is a conjunction or a flip-flop, the third element
# stores the state; for a flip-flop the state is
# initialized to 'off'; for a conjunction, the state
# is a tuple of input modules and the last seen pulse
# from each input (initialized to 'low').
def parseInput(lines, modules):
   conjunctions = []
   # Create an entry for each module
   for line in lines:
      name, action = line.split(' -> ')
      if ',' in action:
         action = tuple(action.split(', '))
      else:
         action = (action,)

      # If the module is a flip-flop, set its initial
      # state to 'low'.
      if name[0] == '%':
         modules[name[1:]] = (name[0], action, 'off')
      elif (name[0] == '&'):
         modules[name[1:]] = (name[0], action, None)
         conjunctions.append(name[1:])
      else:
         modules[name] = (None, action, None)

   # For each conjunction, identify all inputs and add
   # them to the third element of the conjuction with
   # an initial state of 'low'.
   for c in conjunctions:
      inputs = []
      for key in modules:
         action = modules[key][1]
         if c in action:
            inputs.append((key, 0))
      modules[c] = (modules[c][0], modules[c][1], tuple(inputs))

   # Finally, add a module for the button with the
   # initial state set to 'low'.
   modules['button'] = (None, ('broadcaster',), None)

   return modules

         
if __name__ == '__main__':
   lines = readFile("input20b.txt")
   modules = dict()
   parseInput(lines, modules)
   low_count = 0
   high_count = 0

   max_button_push = 1000
   for i in range(max_button_push):
      toVisit = [ (0, 'broadcaster') ]
      # Conduct a breadth-first search through the modules
      # starting with the 'broadcaster' module and a 'low'
      # pulse (resulting from the button push).
      while len(toVisit) > 0:
         # The next data item from toVisit is different
         # depending on if it is visiting a conjunction
         # or not--the conjunction has three data items
         # including the data source, while all other
         # modules only have two.
         if len(toVisit[0]) == 2:
            pulse, current = toVisit.pop(0)
         else:
            pulse, current, inputs = toVisit.pop(0)

         # Based on the current pulse value, increment
         # the appropriate counter.
         if pulse == 0:
            low_count += 1
         else:
            high_count += 1

         # Retrieve the data for the current module
         mod_type, action, state = modules[current]
         
         # If the current module is the 'broadcaster'
         # module, then simply forward the signal to
         # all output modules.
         if current == 'broadcaster':
            # Send the appropriate signal to all output states
            for send in action:
               # If an unknown module is encountered,
               # then add it to the dictionary
               if send not in modules:
                  modules[send] = (None, None, None)

               # If the output module is a conjunction,
               # then include the source of the input
               if modules[send][0] == '&':
                  toVisit.append((pulse, send, current))
               else:
                  toVisit.append((pulse, send))

         # Handle the case in which the current module is
         # a flip-flop
         elif mod_type == '%':
            # If the pulse is low, then flip
            # the state
            if pulse == 0:
               if state == 'off':
                  state = 'on'
                  next_pulse = 1
               elif state == 'on':
                  state = 'off'
                  next_pulse = 0
               else:
                  print('Error: unknown flip-flop state at ' + current)

               # Update the state in the dictionary
               modules[current] = (modules[current][0], modules[current][1], state)

               # Send the appropriate signal to all output states
               for send in action:
                  # If an unknown module is encountered,
                  # then add it to the dictionary
                  if send not in modules:
                     modules[send] = (None, None, None)

                  # If the output module is a conjunction,
                  # then include the source of the input
                  if modules[send][0] == '&':
                     toVisit.append((next_pulse, send, current))
                  else:
                     toVisit.append((next_pulse, send))

            else:
               # Received high pulse in flip-flop, so ignoring
               pass

         # Handle the case in which the current module is
         # a conjunction 
         elif mod_type == '&':
            # Update the state based on the input source
            new_state = []
            all_ones = True
            for s in state:
               if s[0] == inputs:
                  new_state.append((inputs, pulse))
               else:
                  new_state.append(s)

               if new_state[-1][1] != 1:
                  all_ones = False

            # If the conjunction remembers high pulses for all
            # inputs, it sends a low pulse; otherwise, it sends
            # a high pulse.
            if all_ones:
               next_pulse = 0
            else:
               next_pulse = 1

            # Update the state in the dictionary
            modules[current] = (modules[current][0], modules[current][1], tuple(new_state))
            
            # Send the appropriate signal to all output states
            for send in action:
               # If an unknown module is encountered,
               # then add it to the dictionary
               if send not in modules:
                  modules[send] = (None, None, None)

               # If the output module is a conjunction,
               # then include the source of the input
               if modules[send][0] == '&':
                  toVisit.append((next_pulse, send, current))
               else:
                  toVisit.append((next_pulse, send))

         else:
            # An empty module is encountered so do nothing
            pass

   print('low pulse count = ' + str(low_count))
   print('high pulse count = ' + str(high_count))
   print('low count x high count = ' + str(low_count * high_count))

   
   
   
