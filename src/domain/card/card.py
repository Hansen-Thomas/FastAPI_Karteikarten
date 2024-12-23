import datetime

from domain.card.word_type import WordType
from domain.tag.tag import Tag


class Card(object):
    def __init__(self) -> None:
        self.id: int = None
        self.word_type: WordType = WordType.NONE

        self.german: str = ""
        self.italian: str = ""

        self.tags: list[Tag] = []

        self.times_played: int = 0
        self.correct_answers: int = 0
        self.last_answer_correct: bool = False
        self.last_played: datetime.datetime | None = None

    def __repr__(self) -> str:
        return f"Card(id={self.id}, german={self.german}, italian={self.italian})"
    
    def __eq__(self, other: object) -> bool:
        if other is None:
            return False
        elif not isinstance(other, Card):
            return False
        else:
            return self.german == other.german and self.italian == other.italian
        
    def __hash__(self) -> int:
        return hash(self.id)

    def solve(self, solve_italian: bool, guess: str) -> bool:
        if solve_italian:
            solution = self.italian
        else:
            solution = self.german
        correct = True if guess == solution else False
        self.update_statistics(correct)
        return correct

    def update_statistics(self, correct: bool) -> None:
        self.times_played += 1
        if correct:
            self.correct_answers += 1
        self.last_answer_correct = correct
        self.last_played = datetime.datetime.now()

    @property
    def wrong_answers(self) -> int:
        return self.times_played - self.correct_answers

    def add_tag(self, value: str) -> None:
        tag = Tag(value)
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, value: str) -> None:
        tag = Tag(value)
        if tag in self.tags:
            self.tags.remove(tag)

    def has_tag(self, value: str) -> bool:
        tag = Tag(value)
        return tag in self.tags
