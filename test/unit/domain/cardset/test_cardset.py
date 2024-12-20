from domain.cardset.cardset import Cardset
from domain.card.card import Card


def test_cardset():
    card1 = Card()
    card1.german = "die Antwort"
    card1.italian = "la risposta"
    
    card2 = Card()
    card2.german = "die Frage"
    card2.italian = "la domanda"
    
    cardset = Cardset("Test", [card1, card2])
    assert len(cardset) == 2
    assert cardset.get_card(0) == card1
    assert cardset.get_card(1) == card2
    assert cardset.has_card(card1)
    assert cardset.has_card(card2)
    assert not cardset.has_card(Card())
    
    card3 = Card()
    card3.german = "der Hund"
    card3.italian = "il cane"
    cardset.add_card(card3)
    assert len(cardset) == 3
    assert cardset.get_card(2) == card3
    assert cardset.has_card(card3)