from domain.card.card import Card


class Cardset:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards

    def __str__(self):
        return f"{self.name} ({len(self.cards)} cards)"
    
    def __repr__(self):
        return f"Cardset(name={self.name}, cards={self.cards})"
    
    def add_card(self, card: Card) -> None:
        if card not in self.cards:
            self.cards.append(card)
            
    def remove_card(self, card: Card) -> None:
        if card in self.cards:
            self.cards.remove(card)
        
    def has_card(self, card: Card) -> bool:
        return card in self.cards
    
    def get_card(self, index: int) -> Card:
        return self.cards[index]
    
    def pop_card(self, index: int) -> Card:
        return self.cards.pop(index)
    
    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)
        
    def from_tag(self, tag: str) -> list[Card]:
        return [card for card in self.cards if card.has_tag(tag)]
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def get_tags(self) -> set[str]:
        tags = set()
        for card in self.cards:
            tags.update(card.tags)
        return tags
