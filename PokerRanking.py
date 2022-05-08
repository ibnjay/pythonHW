from collections import Counter
from sysconfig import is_python_build

class Card:
    def __init__(self, value, suit):
        """A card is created with Value and Suit string"""
        self.suit = suit

        if value == 'T':
            self.value = 10
        elif value == 'J':
            self.value = 11
        elif value == 'Q':
            self.value = 12
        elif value == 'K':
            self.value = 13
        elif value == 'A':
            self.value = 14
        else:
            self.value = int(value)

        
    def __str__(self):
        return str(self.value) + str(self.suit)


class Hand:

    def __init__(self, list_of_cards):
        """A Hand is crated with a list of Card object"""
        self.list_of_cards = list_of_cards
        self.hand_size = len(list_of_cards)
        self.all_suits = [card.suit for card in self.list_of_cards]
        self.all_value = sorted([card.value for card in self.list_of_cards])
        self.distinct_value = list(set(self.all_value))
        
    def __str__(self):
        return str([str(card) for card in self.list_of_cards])

    def get_all_suits(self):
        return self.all_suits

    def get_all_value(self):
        return self.all_value
    

    def is_flush(self):
        """
        Flush: All cards of the same suit.
        Need highest value card from here to break tie.
        Return Type is Tuple.
        """
        if  len(set(self.get_all_suits())) > 1:
            return (False, -1)
        else:
            return (True, self.highest_value_card() )


    def is_four_of_a_kind(self):
        """
        Four of a Kind: Four cards of the same value.
        Need highest value card from here to break tie.
        Return Type is Tuple.
        """
        if len(self.distinct_value) > 3 :
           return (False, -1)
        else:
            counts = Counter(self.all_value)
            if counts[self.distinct_value[0]] >= 4 :
                return (True, self.distinct_value[0])
            elif counts[self.distinct_value[1]] >= 4:
                return (True, self.distinct_value[1])
            else:
                return (False, -1)

    def is_straight(self):
        """
        Straight: All cards are consecutive values.
         Assume all means if hand size is 7 then all seven have to be consecutive.
        JQKA2 a wrap-around is not assumed to be Straight here.
        Need highest value card from here to break tie.
        Return Type is Tuple.
        """
        if len(self.distinct_value) == len(self.all_value):
            if  self.distinct_value[0] + self.hand_size == self.distinct_value[self.hand_size-1] + 1 :
                return (True, self.highest_value_card())
            else:
                return (False, -1)
        else:
            return (False, -1)


    def is_straight_flush(self):
        """
        Straight Flush: All cards are consecutive values of same suit. 
        Need highest value card from here to break tie.
        Return Type is Tuple.
        """
        if self.is_flush()[0] and self.is_straight()[0] :
            return (True, self.highest_value_card())
        else :
            return (False, -1)


    def is_royal_flush(self):
        """
        Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        Method won't work for larger hand size due to is_flush.
        Can't break ties with this hand.
        """
        if self.is_flush()[0] :
           return all(item in self.all_value for item in [10,11,12,13,14])
        else:
            return False

    def is_one_pair(self):
        """
        One Pair: Two cards of the same value.
        Method should work irrespective of hand size.
        Return False for case where more than  2 cards of same Value.
        Return False if two pairs.
        Need highest value card from here to break tie.
        Return Type is Tuple.

        """
        # count frequency of each value
        items_with_exact_two_counts = [value for value, count in Counter(self.all_value).items() if count == 2]
        if len(items_with_exact_two_counts) == 1:
            tie_breaker_1 = items_with_exact_two_counts[0]
            items_with_exact_one_counts = sorted([value for value, count in Counter(self.all_value).items() if count == 1])
            tie_breaker_2 = items_with_exact_one_counts[-1] if len(items_with_exact_one_counts) != 0 else -1
            return (True, tie_breaker_1, tie_breaker_2)
        else:
            return (False, -1)
    
    def is_two_pair(self):
        """
        Two Pair: Two different pairs.
        Method should work irrespective of hand size.
        Return False for case where more than  2 cards of same Value
        Returns True if three different pairs prerent.
        Need highest value card from here to break tie.
        Return Type is Tuple.

        """
        if len(self.distinct_value) + 1  >=  len(self.all_value) :
            return (False, -1)
        else:
            # count frequency of each value
            items_with_exact_two_counts = sorted([value for value, count in Counter(self.all_value).items() if count == 2])
            if len(items_with_exact_two_counts) >= 2:
                tie_breaker_1 = items_with_exact_two_counts[-1]
                tie_breaker_2 = items_with_exact_two_counts[-2] 
                return (True, tie_breaker_1, tie_breaker_2)
            else:
                return (False, -1)


    def is_three_of_a_kind(self):
        """
        Three of a Kind: Three cards of the same value.
        Method should work irrespective of hand size.
        Return False for case where more than three card of same value.
        Return True if two three of a kind present.
        Return highest value card from here to break tie.
        Return Type is Tuple.

        """
        if len(self.distinct_value) + 1  >=  len(self.all_value) :
            return (False, -1)
        else:
            # count frequency of each value
            items_with_exact_three_counts = [value for value, count in Counter(self.all_value).items() if count == 3]
            if len(items_with_exact_three_counts) >= 1:
                tie_breaker = items_with_exact_three_counts[0]
                return (True, tie_breaker)
            else:
                return (False, -1)
    

    def is_full_house(self):
        """
        Full House: Three of a kind and a pair.
        Note Method would return false if three of a kind and more than one pair present.
        Return highest value card from here to break tie.
        Return Type is Tuple.
        """
        bool_three_of_a_kind, tie_breaker = self.is_three_of_a_kind()
        if bool_three_of_a_kind and self.is_one_pair()[0]:
            return (True, tie_breaker)
        else:
            return (False, -1)
    

    def highest_value_card(self):
        """
        Return Highest value card
        """
        return self.all_value[-1]


    def rank(self):
        
        ROYAL_FLUSH = 100
        STRAIGHT_FLUSH = 90
        FOUR_OF_A_KIND = 80
        FULL_HOUSE = 70
        FLUSH = 60
        STRAIGHT = 50
        THREE_OF_A_KIND = 40
        TWO_PAIRS = 30
        ONE_PAIR = 20

        if self.is_royal_flush(): return (ROYAL_FLUSH, -1)
        elif self.is_straight_flush()[0] : return (STRAIGHT_FLUSH,  self.is_straight_flush()[1])
        elif self.is_four_of_a_kind()[0] : return (FOUR_OF_A_KIND, self.is_four_of_a_kind()[1])
        elif self.is_full_house()[0] : return (FULL_HOUSE, self.is_full_house()[1])
        elif self.is_flush()[0] : return (FLUSH, self.is_flush()[1])
        elif self.is_straight()[0] : return (STRAIGHT, self.is_straight()[1])
        if self.is_three_of_a_kind()[0] : return (THREE_OF_A_KIND, self.is_three_of_a_kind()[1])
        elif self.is_two_pair()[0] : return (TWO_PAIRS, self.is_two_pair()[1])
        elif self.is_one_pair()[0] : return (ONE_PAIR, self.is_one_pair()[1])
        else: return (self.highest_value_card(), -1)



def main(filename='card_game.txt'):
    file_to_read = open(filename, 'r')
    lines = file_to_read.readlines()
    print(len(lines))
    for line in lines:
        # Use rstrip to remove /n newline character. split based on ' '
        all_hands_in_game = line.rstrip().split(' ')
        # print(all_hands_in_game)
        p1_partition = all_hands_in_game[:5]
        p2_partition = all_hands_in_game[5:]

        p1_list_of_cards = [Card(item[0], item[1]) for item in p1_partition]
        p2_list_of_cards = [Card(item[0], item[1]) for item in p2_partition]

        p1_hand = Hand(p1_list_of_cards)
        p2_hand = Hand(p2_list_of_cards)

        print(p1_hand)
        print(p2_hand)
        p1_rank, p1_tb1 = p1_hand.rank()
        p2_rank, p2_tb1 = p2_hand.rank()
        print("RANK P1 : {}. Rank P2 : {} ".format(p1_rank, p2_rank))

        if p1_rank > p2_rank:
            winner = "Player 1"
        elif p2_rank > p1_rank:
            winner = "Player 2"
        else:
            print("TIE")
            if p1_tb1 > p2_tb1 :
                winner = "Player 1"
            elif p1_tb1 < p2_tb1 :
                winner = "Player 2"
            else:
                winner = "TIE"
        print( "Winner of game is : {}".format(winner))

        

if __name__ == "__main__":
    main()
    # test()
