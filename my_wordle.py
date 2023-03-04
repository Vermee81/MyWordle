import string


class MyWordle:
    def __init__(self):
        pass

    def get_alphabet_status(self, input_word: str, answer_word: str) -> str:
        if input_word == "":
            return "\n" + string.ascii_uppercase + "\n" + "?" * 26

        alphabet = string.ascii_uppercase
        answer_string: str = "\n" + string.ascii_uppercase + "\n"

        for letter in alphabet:
            if letter in input_word and letter in answer_word:
                answer_string += "○"
                continue
            if letter in input_word:
                answer_string += "×"
                continue
            answer_string += "?"

        return answer_string
