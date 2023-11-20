import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Club", 8)
        self.card2 = Card("Heart", 5)
        self.card3 = Card("Spade", 2)

    def testCanCheckAce(self):
        test = CardGame.check_for_ace(self, self.card1)      
        self.assertEqual(False, test)

    def testCanGetHighestCard(self):
        test = CardGame.highest_card(self, self.card1, self.card3)
        self.assertEqual(self.card1, test)

    def testCardsTotal(self):
        cards = [self.card1, self.card2, self.card3]
        test = CardGame.cards_total(self, cards)
        self.assertEqual("You have a total of 15", test)
