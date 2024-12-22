from domain.card.card import Card


def check_answer(card: Card, guess: str, ask_for_italian: bool = True) -> None:
    if ask_for_italian:
        correct = card.solve_italian(guess)
    else:
        correct = card.solve_german(guess)
    return correct