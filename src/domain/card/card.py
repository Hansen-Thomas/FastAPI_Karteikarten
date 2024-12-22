import datetime

from domain.card.word_type import WordType


class Card(object):
    def __init__(self) -> None:
        self.id: int = 0
        self.word_type: WordType = WordType.NONE

        self.german: str = ""
        self.italian: str = ""

        self.tags: list[str] = []

        self.times_played: int = 0
        self.correct_answers: int = 0
        self.last_answer_correct: bool = False
        self.last_played: datetime.datetime | None = None

    def __repr__(self) -> str:
        return f"Card(id={self.id}, german={self.german}, italian={self.italian})"
    
    def solve(self, solve_italian: bool, guess: str) -> bool:
        if solve_italian:
            correct = True if guess == self.italian else False
        else:
            correct = True if guess == self.german else False
        self.update_statistics(correct)
        return correct

    def update_statistics(self, correct: bool) -> None:
        self.times_played += 1
        if correct:
            self.correct_answers += 1
        self.last_answer_correct = correct
        self.last_played = datetime.datetime.now()

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags
