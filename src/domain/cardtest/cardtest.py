from domain.card.card import Card
from domain.cardset.cardset import Cardset


class Cardtest:
    
    def __init__(self, name: str, cardset: Cardset):
        self.name = name
        self.cardset = cardset
        self.current_card_index = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.last_answer_correct = False
        
    def __str__(self):
        return f"{self.name} ({self.correct_answers} correct, {self.wrong_answers} wrong)"
    
    def __repr__(self):
        return f"Cardtest(name={self.name}, cardset={self.cardset}, correct_answers={self.correct_answers}, wrong_answers={self.wrong_answers})"
    
    def get_current_card(self) -> Card:
        return self.cardset.get_card(self.current_card_index)