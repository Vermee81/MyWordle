import string
from enum import Enum


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
        self.input_status = {}
        self.attempts = 6

    def update_status(self, input_word: str, answer_word: str):
        self.input_status = {i: STATUS.UNKNOWN for i in input_word}
        for i_l, a_l in zip(input_word, answer_word):
            if i_l == a_l:
                self.input_status[i_l] = STATUS.MATCHED
                self.alphabet_status[i_l] = STATUS.MATCHED
            elif i_l in answer_word:
                self.input_status[i_l] = STATUS.AVAILABLE
                if self.alphabet_status[i_l] != STATUS.MATCHED:
                    self.alphabet_status[i_l] = STATUS.AVAILABLE
            else:
                if (
                    self.alphabet_status[i_l] != STATUS.MATCHED
                    or self.alphabet_status[i_l] != STATUS.AVAILABLE
                ):
                    self.input_status[i_l] = STATUS.MISSING
                    self.alphabet_status[i_l] = STATUS.MISSING

    def get_alphabet_status(self, input_word: str, answer_word: str) -> str:
        self.update_status(input_word, answer_word)
        return self.get_string_status()

    def get_string_status(self) -> str:
        string_status = "\n" + string.ascii_uppercase + "\n"
        for l in string.ascii_uppercase:
            status = self.alphabet_status[l]
            string_status += status.value
        return string_status

    def get_result(self, input_word: str, answer_word: str) -> str:
        ans_string = "\n" + input_word + "\n"
        self.update_status(input_word, answer_word)
        ans_string += "".join([self.input_status[i].value for i in input_word])
        return ans_string

    def is_all_matched(self) -> bool:
        if self.input_status == {}:
            return False
        for val in self.input_status.values():
            if val != STATUS.MATCHED:
                return False
        return True

    def check_game_status(self) -> GameStatus:
        if self.is_all_matched():
            return GameStatus.WIN
        if self.attempts == 0 and not self.is_all_matched():
            return GameStatus.LOSE
        return GameStatus.CONTINUE


if __name__ == "__main__":
    my_wordle = MyWordle()
    my_wordle.answer = "CIDER"
    print("Guess a 5 letter word")
    while my_wordle.check_game_status() == GameStatus.CONTINUE:
        input_str = input()
        print(my_wordle.get_result(input_str, my_wordle.answer))
        print(my_wordle.get_alphabet_status(input_str, my_wordle.answer))
        my_wordle.attempts -= 1

    if my_wordle.check_game_status() == GameStatus.WIN:
        print("You won the game!!!")

    if my_wordle.check_game_status() == GameStatus.LOSE:
        print("You lose. You can try next time.")
