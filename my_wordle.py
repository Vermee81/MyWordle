import string
from enum import Enum


class MyWordle:
    def __init__(self):
        self.alphabet_status = {a: STATUS.UNKNOWN for a in string.ascii_uppercase}
        self.input_status = {}

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


class STATUS(Enum):
    UNKNOWN = "?"
    MATCHED = "O"
    AVAILABLE = "A"
    MISSING = "X"
