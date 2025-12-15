# For each seed value, map the seed through the
# first mapping data, take the output and apply
# it to the next mapping data, etc. until the
# final value is calculated.  From the collection
# of values generated from the seeds, display
# the smallest value.

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
# each value and return it as a list of integers.
def get_seeds(line):
   # The 'seeds' label is separated from the seed
   # values by a colon ':'.
   seeds = line.split(':')
   seeds = seeds[1].split()
   seed_vals = [ int(seed) for seed in seeds ]

   return seed_vals
   

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

   # For each seed value, find the lowest location
   # number that corresponds to any of the initial
   # seeds. To do this, you'll need to convert each
   # seed number through other categories until you
   # can find its corresponding location number.
   #print('Generating locations.')
   locations = []
   for s in seeds:
      t = s
      # Within each map set:
      for m1 in map_set:
         # Find the correct starting range, calculate the
         # offset, and then calculate the corresponding
         # destination value.
         for src, dst, rng in m1:
            if (t >= src) and (t < src + rng):
               t = dst + (t - src)
               break

      locations.append(t)

   # Find the lowest location number that corresponds
   # to any of the initial seed numbers and display it.
   #print(locations)
   print('minimum location = ' + str(min(locations)))
