# 6.00 Problem Set 6
#
# The 6.00 Word Game
#
# Scott Brenner
# Problem 1: 25 minutes
# Problem 2: 35 minutes
# Problem 3: ~8 hours  Lots of careless problems along the way.  Problems cause by short periods of time to work on problems and trouble with large sclae organization.


import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
COMPUTER_TIME_FACTOR = 1

SCRABBLE_LETTER_VALUES = {
'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# PREPROCESSSING FUNCTIONS- These prep the word lists/dictionaries for game play.  They should execute only once--when the app is launched.  They include function used for scoring and for the computer-player.
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def sort_word(word_string):
    """
    Takes a string, alphabetizes it and returns it as a string.
    """
    char_list =[]
    sorted_string = ''
    for char in word_string:
        char_list.append(char)
    char_list.sort()
    for char in char_list:
        sorted_string += char
    return sorted_string

def get_word_rearrangements(a_list_of_words):
    """
    This function takes a list of words and returns a dictionary of strings mapped to actual words.
    
    This function is used by the computer-player to find valid words.
    
    Create a dict where, for any set of letters, you can determine if there is some acceptable word that is a rearrangement of those letters.
    Let d = {}
    For every word w in the word list:
        Let d[(string containing the letters of w in sorted order)] = w
    """
    rearrange_dict = {}
    for word in a_list_of_words:
        #   build a list from the char in word: 1) convert word string to list, 2) sort list, 3) convert list back to string.
        char_list =[]
        my_string = ''
        for char in word:
            char_list.append(char)
        char_list.sort()
        for each in range(len(char_list)):
            my_string +=char_list[each]
        rearrange_dict[my_string] = word
    #print "In get_word_rearrangements. Rrearrange_dict:", rearrange_dict
    return rearrange_dict

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    
    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.
    
    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    
    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    return score


# -----------------------------------
# GAME PLAY FUNCTIONS- These functions start and play the game play.  They will execute mulitple times.
def display_hand(hand):
    """
    Displays the letters currently in the hand.
    
    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
    
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )

def is_valid_word(word, hand, point_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)                 # Create dictionary frequency dictionary for word.  E.g., if work is 'hello', freq = {'h': 1, 'e': 1, 'l': 2, 'o': 1}.
    for letter in word:
        if freq[letter] > hand.get(letter, 0):      # Confirm that each letter needed to spell word is in the hand in sufficient quantity.
            return False
    return word in point_dict

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    
    * The user may input a word.
    
    * An invalid word is rejected, and a message is displayed asking the user to choose another word.
    
    * When a valid word is entered, it uses up letters from the hand.
    
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    
    * The sum of the word scores is displayed when the hand finishes.
    
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.
      
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """    
    
    total_points = 0.0
    initial_handlen = sum(hand.values())
    foo = True
    elapsed_time = 0.0
    chessTime = get_time_limit(point_dict, COMPUTER_TIME_FACTOR)
    print "\nComputer will have %0.2f seconds to play the hand.\n" % chessTime
    # this is commented out because it was replaced by the line above.  The line above sets chessTime based on computer speed.  The commented code aske the user for chessTime.
    # while foo:
    #     chessTime = raw_input('Enter time limit, in seconds, for players:')
    #     if chessTime.isdigit():
    #         chessTime = float(chessTime)
    #         foo = False
    while sum(hand.values()) > 0:
        print
        print 'Current Hand:',
        display_hand(hand)
        startTime = time.time()
        # userWord = raw_input('Enter word, or a . to indicate that you are finished: ')
        userWord = pick_best_word_faster(hand, arranged_words) # 'faster' function
        # userWord = pick_best_word(hand, point_dict) # orignial fuction
        endTime = time.time()
        playTime = endTime - startTime
        print "It took %0.5f seconds to play %s." % (playTime, userWord)
        elapsed_time += playTime
        if userWord == '.':
            break
        elif elapsed_time > chessTime:
            print "It took %0.5f seconds to play %s." % (playTime, userWord)
            # print 'It took %0.2f seconds to enter your word.' % elapsed_time
            print 'Your total time to play the hand exceeded %0.5f seconds. Your final score is %0.2f points.' % (chessTime, total_points)
            break
        else:
            isValid = is_valid_word(userWord, hand, word_list)
            if not isValid:
                print 'Invalid word, please try again.'
            else:
                if playTime < 1: playTime = 1
                points = get_word_score(userWord, initial_handlen) /  playTime
                total_points += points
                print '%s earned %0.5f points. Total: %0.5f points' % (userWord, points, total_points)
                hand = update_hand(hand, userWord)
                #print 'Updated hand:%s' % hand
    print 'Total score: %0.5f points.' % total_points
    return total_points

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
    * Asks the user to input 'n' or 'r' or 'e'.
    
    * If the user inputs 'n', let the user play a new (random) hand. When done playing the hand, ask the 'n' or 'e' question again.
    
    * If the user inputs 'r', let the user play the last hand again.
    
    * If the user inputs 'e', exit the game.
    
    * If the user inputs anything else, ask them again.
    """
    
    # hand_score = 0.0
    # counter = 0
    # while hand_score < 40 or counter < 5:
    #         hand = deal_hand(HAND_SIZE)
    #         hand_score = play_hand(hand.copy(), word_list)
    #         print "Counter %i." %counter 
    #         counter += 1
    # print "Counter %i." %counter 
    
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

# -----------------------------------
# COMPUTER PLAYER FUNCTIONS- These functions play the computer's hand.  They find and play the best word.  They will execute mulitple times.
def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the given hand.
    
    Return '.' if no words can be made with the given hand.
    """
    freq = get_frequency_dict(hand)     # Create dictionary frequency dictionary for the hand
    best_word = ""
    best_word_value = 0
    for word in points_dict:
        if is_valid_word(word, hand, points_dict):
            word_value = get_word_score(word, HAND_SIZE)
            #print "The word is %s, with value %i.   The best word is %s, with value %i." % (word, word_value, best_word, best_word_value)
            if word_value > best_word_value:
                best_word = word
                best_word_value = word_value
    if best_word_value > 0:
        return best_word
    return "."

def get_words_to_point(word_list):
    """
    Return a dict that maps every word in word_list to its point value.
    """
    word_value_dictionary = {}
    for word in word_list:
        word_value_dictionary[word] = get_word_score(word, 7)
    return word_value_dictionary
    #return len(word_value_dictionary)

def pick_best_word_faster(hand, rearrange_dict):
    """
    Takes a hand {dictionary} and a dictionary of letter combinations that map to a valid word.
    
    Returns the highest value word or '.'-if there is no valid word possible.
    
    Pseudo-code:
    To find some word that can be made out of the letters in HAND:
        For each subset S of the letters of HAND:
            Let w = (string containing the letters of S in sorted order)
            If w in d:
                return d[w]
                
    This function must convert the hand{dictionary} to a string.  In doing so it must check to make sure that the value of each key in the had is > 0
    """
    #print "In pick best. Hand:", hand
    hand_string = ''
    
    for each in hand:
        if hand[each] > 0:
            hand_string += each * hand[each]
        
    #print "Hand sorted: %s" %hand_string
    
    best_word =''
    best_word_score = 0
    subsets = build_substrings(hand_string)
    subset_value = 0
    
    for subset in subsets:
        sorted_subset = sort_word(subset)
        if sorted_subset in rearrange_dict:
            subset_value = get_word_score(sorted_subset, HAND_SIZE)
            if subset_value > best_word_score:
                best_word = rearrange_dict[sorted_subset]                
                best_word_score = subset_value
    
    if best_word_score > 0:
        return best_word
    else:
        return '.'

def get_time_limit(points_dict, k): 
    """
    Return the time limit for the computer player as a function of the multiplier k.
    
    points_dict should be the same dictionary that is created by get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k

def build_substrings(string):
    """
    Works on the premiss that given a set of the substrings of a string the
    the subsets of a string with one more char is the formed by taking all the
    substrings in the known subset and also adding to them the set formed by
    adding the character to every element in the old set and then adding the 
    new char.
    
    """
    result = []
    if len(string) == 1:
        result.append(string)
    else:
        for substring in build_substrings(string[:-1]):
            result.append(substring)
            substring = substring + string[-1]
            result.append(substring)
        result.append(string[-1])
        result = list(set(result))  # Convert result into a set.  Sets have no duplicates. Then convert back to list.
        result.sort()
    # now iterate through substrings and sort the characters of each substring    
    #for each in 
    return result


# -----------------------------------
# PLAY GAME: Build data structures used for entire session and play game.
#
if __name__ == '__main__':
    word_list = load_words()
    point_dict = get_words_to_point(word_list)
    arranged_words = get_word_rearrangements(word_list)
    #print len(arranged_words)
    play_game(word_list)




## Problem 5 ##
# your response here.
# as many lines as you want.
# 
# pick_best_word()
#     This method creates a dictionary of every valid word mapped to the point value.  Then it iterates through the dictionary comparing the hand to the word.  If they word can be made from the hand then the word's score is compared to the word score of the earlier possible word.  The higher score word is retained.
#     Under this method the point value dictionary must be built and then the function iterates through comparing the hand to eveyr possible word.
#     Amortizing the time-cost of building the dictionary over each pick, the time complexity of this method grows with the length of the word list and independently from the size of the hand.  Adding letters to the hand will increase the time to execute but only negligibly.  I think the computational complexity of the function is linear.
# 
#   With a hand size of 7 letters the time to pick best word was less than .6 seconds.
#   With a hand size of 17 letters the time to pick best word was ~.6 seconds.
#   With a hand size of 25 letters the time to pick best word was ~.65 seconds.



#     
# pick_best_word_faster()
#   This method also begins by creating a dictionary.  Each value in the dictioanry is a valid word.  Each key is a alphabetized string of the letters in the word. E.g., {'acot':'taco'}.  Note that each key is unique but the value isn't necessarily unique.  The dictionary value for 'acot' could be 'coat'.  This is because the dictionary only needs to list every valid alpahbetized string of letters.  Not ever valid word.  This makes the dictionary the same size or shorter than the dictionary created in pick_best_word().  For the word list used in this problem the savings is ~14,000 entries (83667 words, 69091 dict keys)
#     Armed with this dictionary the function can take advantage of the speed of the "in dictionary" function, which I thinks is logarithmic.  The next part of this function is build a set of substrings of hand.  The function then iterates through this set of substrings checking if they are in the dictionary, and comparing their point value to the prior highest value string in the dictionary.  The function returns the highest point value value from the dictionary.
#     This method is much faster than pick_best_word() because is takes adavantice of the bysect search functionality built into search dicstionaries.  This bysect search algorithm grow logarithmically based on the length of dictionary.
#   Adding letters to the hand will increase the time to execute the function that creates the subsets, but they dicitonary search is the more significant funciton.  I think the computational complexity of the function is logarithmic.

#   With a hand size of 7 letters the time to pick best word was less than .001 seconds.
#   With a hand size of 17 letters the time to pick best word was between .3 and .5 seconds.
#   With a hand size of 25 letters the time to pick best word was between 15 and 45 seconds.

#   Comparing the two functions, it appears the pick_best_word_faster() is much faster for relatively small hands and any size dictionary.  But pick_best_word() is faster if the hands will be large.  Not surprisingly the 'better' function depends on the specifics of the problem.