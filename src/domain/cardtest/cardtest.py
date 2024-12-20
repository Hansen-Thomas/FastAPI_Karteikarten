from domain.card.card import Card
from domain.cardset.cardset import Cardset


class Cardtest:
    
    def __init__(self, name: str, cardset: Cardset) -> None:
        self.name: str = name
        self.cardset: Cardset = cardset
        self.current_card_index: int = 0
        self.correct_answers: int = 0
        self.wrong_answers: int = 0
        self.last_answer_correct: bool = False
        
    def __str__(self):
        return f"{self.name} ({self.correct_answers} correct, {self.wrong_answers} wrong)"
    
    def __repr__(self):
        return f"Cardtest(name={self.name}, cardset={self.cardset}, correct_answers={self.correct_answers}, wrong_answers={self.wrong_answers})"
    
    def get_current_card(self) -> Card:
        return self.cardset.get_card(self.current_card_index)