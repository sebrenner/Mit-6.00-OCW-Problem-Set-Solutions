from ps5 import *

#
# Test code
#
def test_deal_hand():
    """
    Unit test for deal_hand.
    """
    
    # (A)
    # Basic test, see if the right kind of dictionary is
    # being returned.
    hand = deal_hand(HAND_SIZE)
    if not type(hand) is dict:
        print "FAILURE: test_deal_hand()"
        print "\tUnexpected return type:", type(hand)
        
        return # exit function

    num = 0
    for k in hand.keys():
        if (not type(k) is str) or (not type(hand[k]) is int):
            print "FAILURE: test_deal_hand()"
            print "\tUnexpected type of dictionary: string -> int expected, but was", type(k), "->", type(hand[k])

            return # exit function
        elif not k in "abcdefghijklmnopqrstuvwxyz":
            print "FAILURE: test_deal_hand()"
            print "\tDictionary keys are not lowercase letters."

            return # exit function
        else:
            num += hand[k]
            
    if num != HAND_SIZE:
            print "FAILURE: test_deal_hand()"
            print "\tdeal_hand() returned more letters than it was asked to."
            print "\tAsked for a hand of size", HAND_SIZE, "but it returned a hand of size", num

            return # exit function
        
    # (B)
    # Tests randomness..
    repeats=0
    hand1 = deal_hand(HAND_SIZE)
    for i in range(20):                
        hand2 = deal_hand(HAND_SIZE)
        if hand1 == hand2:
            repeats += 1
        hand1 = hand2
        
    if repeats > 10:
        print "FAILURE: test_deal_hand()"
        print "\tSame hand returned", repeats, "times by deal_hand(). This is HIGHLY unlikely."
        print "\tIs the deal_hand implementation really using random numbers?"

        return # exit function
    
    print "SUCCESS: test_deal_hand()"

def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):2, ("was", 7):6, ("scored", 7):9, ("waybill", 7):65, ("outgnaw", 7):61, ("outgnawn", 8):62}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print "FAILURE: test_get_word_score()"
            print "\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n)
            failure=True
    if not failure:
        print "SUCCESS: test_get_word_score()"

def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    word = "quail"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print "FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")"
        print "\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2

        return # exit function
        
    # test 2
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print "FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")"        
        print "\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2

        return # exit function

    # test 3
    hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    word = "hello"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print "FAILURE: test_update_hand('"+ word +"', " + str(hand) + ")"                
        print "\tReturned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2
        
        return # exit function

    print "SUCCESS: test_update_hand()"

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    hand = get_frequency_dict(word)

    if not is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand

        failure = True

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected True, but got False for word: '"+ word +"' and hand:", hand

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"
    
    if  not is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected True, but got False for word: '" + word + "' and hand:", hand
        
        failure = True
        
    # test 6
    word = "even"

    if  is_valid_word(word, hand, word_list):
        print "FAILURE: test_is_valid_word()"
        print "\tExpected False, but got True for word: '" + word + "' and hand:", hand
        print "\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)"        
        
        failure = True        

    if not failure:
        print "SUCCESS: test_is_valid_word()"


word_list = load_words()
print "----------------------------------------------------------------------"
print "Testing get_word_score..."
test_get_word_score()
print "----------------------------------------------------------------------"
print "Testing update_hand..."
test_update_hand()
print "----------------------------------------------------------------------"
print "Testing is_valid_word..."
test_is_valid_word(word_list)
print "----------------------------------------------------------------------"
print "All done!"
