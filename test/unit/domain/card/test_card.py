from domain.card.card import Card


def test_create_simple_card():
    card = Card()
    card.german = "die Antwort"
    card.italian = "la risposta"
    assert card.solve(solve_italian=True, guess="la risposta")
    assert not card.solve(solve_italian=True, guess="la domanda")


def test_create_card_with_tags():
    card = Card()
    card.add_tag("tag1")
    card.add_tag("tag2")
    assert card.has_tag("tag1")
    assert card.has_tag("tag2")
    assert not card.has_tag("tag3")
    card.remove_tag("tag1")
    assert not card.has_tag("tag1")
    assert card.has_tag("tag2")
    card.remove_tag("tag2")
    assert not card.has_tag("tag2")
