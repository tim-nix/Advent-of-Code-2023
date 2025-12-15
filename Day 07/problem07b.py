# Calculate the score based on the rank ordering of
# the hands. Rank order the hands first based on the
# hand type (from high card to five of a kind). But,
# for this problem, jokers are treated as wild cards
# so the hand type classification must also consider
# how many jokers are in the hand. Then rank order
# based on card value for hands of the same type.
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


# Convert the data input into the hand (as a string)
# and the bid (as an integer). Then for each hand,
# determine the hand type and store as a tuple.
def parseInput(lines):
   # Convert each hand and bid into a list of tuples.
   hands1 = [ line.split() for line in lines ]
   hands2 = [ (hand, int(bid)) for hand, bid in hands1 ]

   # For each hand, determine the hand type and store
   # the hand type along with the hand and bid.
   # ( type, hand, bid )
   hands3 = []
   for hand, bid in hands2:
      hand_type = getType(hand)
      hands3.append((hand_type, hand, bid))

   return hands3


# For a given hand, determine the scoring of the hand;
# that is, determine if the hand is (in order, from
# lowest to highest) high card only, one pair, two
# pairs, three of a kind, full house, four of a kind,
# or five of a kind. However, now Jokers are wild.
def getType(hand):
   hand_list = list(hand)

   # Count the number of jokers in the hand.
   jokers = 0
   for card in hand_list:
      if card == 'J':
         jokers += 1

   # Convert the hand into a set (which will not
   # contain duplicates). Score the hand based, in
   # part, on the size of the set.
   hand_set = set(hand_list)
   hand_type = ''

   # All cards are different and no jokers.
   if (len(hand_set) == 5) and (jokers == 0):
      hand_type = 0 # "High card"

   # Two cards must have been the same or all
   # different with one joker.
   elif ((len(hand_set) == 5) and (jokers == 1)) or ((len(hand_set) == 4) and (jokers == 0)):
      hand_type = 1 # "One pair"

   # Either two pairs of cards were the same, or
   # three cards were the same with no jokers in
   # either case.
   elif ((len(hand_set) == 3) and (jokers == 0)):
      max_count = 0
      for card in hand_list:
         if hand_list.count(card) > max_count:
            max_count = hand_list.count(card)
      if max_count == 2:
         hand_type = 2 # "Two pair"
      elif max_count == 3:
         hand_type = 3 # "Three of a kind"

   # Either one pair and one joker or only a pair
   # of jokers.
   elif ((len(hand_set) == 4) and (jokers == 1)) or ((len(hand_set) == 4) and (jokers == 2)):
      hand_type = 3 # "Three of a kind"

   # Either three cards were the same and two
   # other cards were the same, or four cards
   # were the same with no jokers in either
   # case.
   elif (len(hand_set) == 2) and (jokers == 0):
      max_count = 0
      for card in hand_list:
         if hand_list.count(card) > max_count:
            max_count = hand_list.count(card)
      if max_count == 3:
         hand_type = 4 # "Full house"
      elif max_count == 4:
         hand_type = 5 # "Four of a kind"

   # Either one pair plus a pair of jokers or
   # no matching cards except for three jokers.
   elif ((len(hand_set) == 3) and (jokers == 2)) or ((len(hand_set) == 3) and (jokers == 3)):
      hand_type = 5 # "Four of a kind"

   # Either three cards were the same and two
   # other cards were the same, or four cards
   # were the same.
   elif ((len(hand_set) == 3) and (jokers == 1)):
      max_count = 0
      for card in hand_list:
         if hand_list.count(card) > max_count:
            max_count = hand_list.count(card)
      if max_count == 2:
         hand_type = 4 # "Full house"
      elif max_count == 3:
         hand_type = 5 # "Four of a kind"

   # All five cards must be the same or one card
   # value plus enough jokers.
   elif (len(hand_set) == 1) or ((len(hand_set) == 2) and (jokers >= 1)):
      hand_type = 6 # "Five of a kind"

   # Should not be needed, but is included for
   # error checking.
   else:
      print("No hand type assigned")
      print("case = " + str(hand))

   return hand_type


# Compare two hands and determine if hand1 has a
# card of higher value than hand2.
def isBigger(hand1, hand2):
   # Define the card ranking.
   card_order = [ 'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A' ]

   # Iterate through the cards until the card in
   # hand1 is different from the card in hand2.
   hand_list1 = list(hand1)
   hand_list2 = list(hand2)
   for i in range(len(hand_list1)):
      if hand_list1[i] !=  hand_list2[i]:
         index1 = card_order.index(hand_list1[i])
         index2 = card_order.index(hand_list2[i])

         # If the card in hand1 is of higher
         # value than the corresponding card
         # in hand2, then return True.
         # Otherwise, return False.
         if index1 > index2:
            return True
         else:
            return False

   print("Two hands are identical.")
   return None
   

# Perform a simple bubble sort on the hands based
# on the card values (not the hand). We are more
# interested in determining order among all cards
# of the same hand type.
def sortHands(hands):
   for i in range(len(hands)):
      for j in range(len(hands) - i - 1):
         if hands[j][0] == hands[j + 1][0]:
            if isBigger(hands[j][1], hands[j + 1][1]):
               hands[j], hands[j + 1] = hands[j + 1], hands[j]

   return hands
         

# Determine the total winnings of this set of
# hands by adding up the result of multiplying
# each hand's bid with its rank.
def calcScore(sorted_hands):
   score = 0
   rank = 1
   for hand in sorted_hands:
      score += rank * hand[2]
      rank += 1

   return score


if __name__ == '__main__':
   start_time = time.time()
   # Define the hand ordering.
   hand_values = [ "High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind" ]
   lines = readFile("input7b.txt")

   # Convert the file input and classify each hand.
   hands = parseInput(lines)

   # Sort the hands based on the hand type from
   # lowest (High card) to highest (Five of a kind).
   hands.sort()

   # Now sort the hands based on card value within
   # the hand (this sorts the hands within the same
   # hand type).
   sorted_hands = sortHands(hands)

   # Calculate the score and display the result.
   score = calcScore(hands)
   print('score = ' + str(score))
   
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
