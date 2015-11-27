# Methods to check if cards are certain hand
# Suits: S, D, C, H
# ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, J (11), Q (12), K (13), A (14)

from collections import namedtuple
from collections import defaultdict 
from functools import total_ordering

class RankException(Exception):
  pass

class SuitException(Exception):
  pass

ranks = '2.3.4.5.6.7.8.9.10.J.Q.K.A'.split('.')
Card = namedtuple('Card', ['rank', 'suit'])

@total_ordering
class Card(object):
  ranks = '2.3.4.5.6.7.8.9.10.J.Q.K.A'.split('.')
  suits = 'CSDH'

  def __init__(self, original_card):
    original_rank, original_suit = original_card
    if original_rank not in self.ranks:
      raise RankException('%s is not a possible rank' % original_rank)
    if original_suit not in self.suits:
      raise SuitException('%s is not a possible suit' % original_suit)
    self.original_card = original_card
    self.rank = original_rank
    self.suit = original_suit
    self.computed_rank = self.ranks.index(self.rank)

  def __eq__(self, other):
    return self.rank == other.rank

  def __lt__(self, other):
    return self.computed_rank < other.computed_rank

def highcard(hand):
  return max([Card(card) for card in hand.split(' ')])

def flush(hand):
  return len(set([Card(c).suit for c in hand])) == 1

def straight(hand):
  ranks = sorted([Card(c).computed_rank for c in hand])
  return all([(r[i] - r[i - 1]) == 1 for i in range(1, len(ranks))])

def straight_flush(hand):
  return flush(hand) and straight(hand)

def royal_flush(hand):
  royal_ranks = '10.J.Q.K.A'
  return straight_flush(hand) and all([Card(c).rank in royal_ranks for c in hand])

def process_hand(hand):
  cards = [Card(c) for c in hand]
  ordering = defaultdict(list)
  for c in cards:
    ordering[c.rank] += [c]
  structures = {
      (1,1,1,1,1): [royal_flush, straight_flush, flush, straight, highcard],
      (1,1,1,2): [one_pair],
      (1,2,2): [two_pair],
      (1,1,3): [three_of_a_kind],
      (2,3): [full_house],
      (1,4): [four_of_a_kind]
      }
  hand_structure = sorted(map(len, ordering.values()))
  possible_hands = structures[hand_structure]

