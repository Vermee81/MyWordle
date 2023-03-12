import string
from enum import Enum


class MyWordle:
    def __init__(self):
        self.alphabet_status = {a: STATUS.UNKNOWN for a in string.ascii_uppercase}

    def get_alphabet_status(self, input_word: str, answer_word: str) -> str:
        for i_l, a_l in zip(input_word, answer_word):
            if i_l == a_l:
                self.alphabet_status[i_l] = STATUS.MATCHED
                continue
            if i_l in answer_word:
                self.alphabet_status[i_l] = STATUS.AVAILABLE
                continue
            self.alphabet_status[i_l] = STATUS.MISSING

        return self.get_string_status()

    def get_string_status(self) -> str:
        string_status = "\n" + string.ascii_uppercase + "\n"
        for l in string.ascii_uppercase:
            status = self.alphabet_status[l]
            string_status += status.value
        return string_status

    def get_result(self, input_word: str, answer_word: str) -> str:
        ans_string = "\n" + input_word + "\n"
        for i_l, a_l in zip(input_word, answer_word):
            if i_l == a_l:
                ans_string += STATUS.MATCHED.value
            elif i_l in answer_word:
                ans_string += STATUS.AVAILABLE.value
            else:
                ans_string += STATUS.MISSING.value
        return ans_string


class STATUS(Enum):
    UNKNOWN = "?"
    MATCHED = "O"
    AVAILABLE = "A"
    MISSING = "X"
