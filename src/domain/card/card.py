import datetime

class Card(object):
    def __init__(self) -> None:
        self.id: int = 0
        self.german: str = ""
        self.italian: str = ""
        self.tags: list[str] = []
        self.last_tested: datetime.datetime | None = None
        self.correct_answers: int = 0
        self.wrong_answers: int = 0
        self.last_answer_correct: bool = False
        
    def __repr__(self) -> str:
        return f"Card(id={self.id}, german={self.german}, italian={self.italian})"
    
    def solve_italian(self, italian_guess: str) -> bool:
        return self.italian == italian_guess
    
    def solve_german(self, german_guess: str) -> bool:
        return self.german == german_guess
    
    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)
            
    def remove_tag(self, tag: str) -> None:
        if tag in self.tags:
            self.tags.remove(tag)
            
    def has_tag(self, tag: str) -> bool:
        return tag in self.tags
