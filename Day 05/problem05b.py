# Apply each mapping (one at a time) to the list of
# seed ranges and build a new collection of ranges
# based off of the mapping. Repeat until all mappings
# are applied. Find the smallest lower bound among
# the completed mappings and display it.


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


# From the line of data input that contains the
# seed values (represented as a string), extract
# each pair of numbers. The first value is the
# start of the range and the second value is the
# length of the range. Return a list of tuples
# with each tuple consisting of two integers;
# the start of the range and the end of the
# range (using the start of the range and the
# length of the range to calculate the end).
def get_seeds(line):
   # The 'seeds' label is separated from the seed
   # values by a colon ':'.
   seeds = line.split(':')
   seeds = seeds[1].split()
   seed_vals = [ int(seed) for seed in seeds ]
   seed_pairs = []
   for i in range(0, len(seed_vals), 2):
      seed_pairs.append((seed_vals[i], seed_vals[i] + seed_vals[i + 1]))
      

   return seed_pairs
   

# From a line of data that contains a mapping
# from one type of condition to another (e.g.,
# seed-to soil map').  Each line within a map
# contains three numbers: the destination range
# start, the source range start, and the range
# length.  Return these values as a tuple of
# integers.
def get_map(line):
   values = line.split()
   dst = int(values[0])
   src = int(values[1])
   rng = int(values[2])

   return (src, dst, rng)


if __name__ == '__main__':  
   lines = readFile("input5b.txt")
   # Extract the seed data from the first line
   # of input.
   seeds = get_seeds(lines[0])

   # Generate the mappings.
   #print('Generating mappings.')
   map_set = []
   mapping = []
   for i in range(1, len(lines)):
      line = lines[i]
      # Different mappings are separated by empty
      # lines of string (i.e., '').
      if line == '':
         # If an empty line is encountered but it
         # is not the first empty line, then add
         # the mapping to the map_set.
         if len(mapping) > 0:
            map_set.append(mapping)
      # The first line of the mapping information
      # is the title label of the specific mapping.
      # We ignore the label and prepare for the
      # lines of data that follow it.
      elif 'map' in line:
         mapping = []
      # If the data is mapping data, convert it to
      # a tuple of integers and add it to the list
      # of mapping data.
      else:
         mapping.append(get_map(line))

   # Add the last round of mapping data to the
   # map_set.
   map_set.append(mapping)

   # Apply each map_set to the seeds:
   count = 0
   for m1 in map_set:
      count += 1
      #print('pass ' + str(count) + ' of ' + str(len(map_set)))
      mapped_values = []
      while len(seeds) > 0:
         seed_lower, seed_upper = seeds.pop(0)
         #print('seed = ' + str((seed_lower, seed_upper)))
      
         # Determine if the mapping applies, split the seed
         # range, if necessary, and apply the mapping.
         for src, dst, rng in m1:
            #print('rule = ' + str((src, dst, rng)))
            # Find the overlap, if any.
            overlap_lower = max(seed_lower, src)
            overlap_upper = min(seed_upper, src + rng)
            # When the overlap is found, apply it to the
            # applicable seed range.
            if overlap_lower < overlap_upper:
               mapped_values.append((dst + (overlap_lower - src), dst + (overlap_upper - src)))
               # For the seed range outside of the overlap,
               # return it to the pool of seeds for later
               # mapping.
               if overlap_lower > seed_lower:
                  seeds.append((seed_lower, overlap_lower))
               if seed_upper > overlap_upper:
                  seeds.append((overlap_upper, seed_upper))
               break
         # Any source numbers that aren't mapped correspond to
         # the same destination number, so if a mapping is not
         # found, just reappend the seed range.
         else:
            mapped_values.append((seed_lower, seed_upper))

      seeds = mapped_values
            
   # Find the lowest location number that corresponds
   # to any of the initial seed numbers and display it.
   #print(locations)
   print('minimum location = ' + str(min(seeds)[0]))
         
               
