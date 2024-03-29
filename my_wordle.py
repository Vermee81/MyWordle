import string
from enum import Enum
from random import choice
from word_list import WORD_LIST


class GameStatus(Enum):
    WIN = 0
    LOSE = 1
    CONTINUE = 2


class STATUS(Enum):
    UNKNOWN = "?"
    MATCHED = "O"
    AVAILABLE = "A"
    MISSING = "X"


class MyWordle:
    def __init__(self):
        self.answer = ""
        self.alphabet_status = {a: STATUS.UNKNOWN for a in string.ascii_uppercase}
        self.input_status = []
        self.attempts = 6

    def update_status(self, input_word: str, answer_word: str):
        self.input_status = [[i, STATUS.UNKNOWN] for i in input_word]
        for i, (i_l, a_l) in enumerate(zip(input_word, answer_word)):
            if i_l == a_l:
                self.input_status[i][1] = self.alphabet_status[i_l] = STATUS.MATCHED
            elif i_l in answer_word:
                self.input_status[i][1] = STATUS.AVAILABLE
                if self.alphabet_status[i_l] != STATUS.MATCHED:
                    self.alphabet_status[i_l] = STATUS.AVAILABLE
            else:
                if self.alphabet_status[i_l] not in (STATUS.MATCHED, STATUS.AVAILABLE):
                    self.input_status[i][1] = STATUS.MISSING
                    self.alphabet_status[i_l] = STATUS.MISSING

    def get_alphabet_status(self, input_word: str, answer_word: str) -> str:
        self.update_status(input_word, answer_word)
        return f"\n{string.ascii_uppercase}\n" + "".join(
            status.value for status in self.alphabet_status.values()
        )

    def get_result(self, input_word: str, answer_word: str) -> str:
        self.update_status(input_word, answer_word)
        return f"\n{input_word}\n" + "".join(
            status.value for _, status in self.input_status
        )

    def is_all_matched(self) -> bool:
        if not self.input_status:
            return False
        return all(status == STATUS.MATCHED for _, status in self.input_status)

    def check_game_status(self) -> GameStatus:
        if self.is_all_matched():
            return GameStatus.WIN
        if self.attempts == 0 and not self.is_all_matched():
            return GameStatus.LOSE
        return GameStatus.CONTINUE


if __name__ == "__main__":
    my_wordle = MyWordle()
    my_wordle.answer = str.upper(choice(WORD_LIST))
    print("Guess a 5 letter word")
    while my_wordle.check_game_status() == GameStatus.CONTINUE:
        input_str = str.lower(input())
        if input_str not in WORD_LIST:
            print("It is not in my word list. Please try another word.")
            continue
        input_str = str.upper(input_str)
        print(my_wordle.get_result(input_str, my_wordle.answer))
        print(my_wordle.get_alphabet_status(input_str, my_wordle.answer))
        my_wordle.attempts -= 1

    if my_wordle.check_game_status() == GameStatus.WIN:
        print("You won the game!!!")
    else:
        print(f"You lose. The answer was {my_wordle.answer}. You can try next time.")
