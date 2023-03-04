import pytest
import string
from my_wordle import MyWordle
from my_wordle import STATUS


@pytest.fixture
def my_wordle():
    return MyWordle()


# 入力した単語の文字が正解に使われているかわかったら○、使われていないなら×、不明なら?となっているアルファベットに対応した文字列を返す
# 何も入力されていない状態の時は全部 "?" の文字列を返す
def test_何も入力されていない時はハテナを返す(my_wordle):
    input_word = ""
    answer_word = "RIGHT"
    gotten = my_wordle.get_alphabet_status(input_word, answer_word)
    expected_string = "\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n??????????????????????????"
    assert gotten == expected_string


# 入力した単語が正解の単語とDとRとIが一致していたらDとRとIの位置にOをつけた文字を返す。使っていないVとEの位置にはXを返す。
def test_使っていればマル使っていなければバツ(my_wordle):
    input_word = "DRIVE"
    answer_word = "DRINK"
    gotten = my_wordle.get_alphabet_status(input_word, answer_word)
    expected_string = "\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n???OX???O????????O???X????"
    assert gotten == expected_string


# アルファベットの正答状態から画面に表示する文字列を返す
def test_どの文字も使うかどうかわからない状態の時は全部はてな(my_wordle):
    status = {a: STATUS.UNKNOWN for a in string.ascii_uppercase}
    my_wordle.alphabet_status = status
    expected_string = "\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n??????????????????????????"
    gotten = my_wordle.get_string_status()
    assert gotten == expected_string


def test_DとRとIがMATCHしててAとBがAVAILABLEでCがMISSINGで他ははてな(my_wordle):
    status = {
        "A": STATUS.AVAILABLE,
        "B": STATUS.AVAILABLE,
        "C": STATUS.MISSING,
        "D": STATUS.MATCHED,
        "E": STATUS.UNKNOWN,
        "F": STATUS.UNKNOWN,
        "G": STATUS.UNKNOWN,
        "H": STATUS.UNKNOWN,
        "I": STATUS.MATCHED,
        "J": STATUS.UNKNOWN,
        "K": STATUS.UNKNOWN,
        "L": STATUS.UNKNOWN,
        "M": STATUS.UNKNOWN,
        "N": STATUS.UNKNOWN,
        "O": STATUS.UNKNOWN,
        "P": STATUS.UNKNOWN,
        "Q": STATUS.UNKNOWN,
        "R": STATUS.MATCHED,
        "S": STATUS.UNKNOWN,
        "T": STATUS.UNKNOWN,
        "U": STATUS.UNKNOWN,
        "V": STATUS.UNKNOWN,
        "W": STATUS.UNKNOWN,
        "X": STATUS.UNKNOWN,
        "Y": STATUS.UNKNOWN,
        "Z": STATUS.UNKNOWN,
    }
    my_wordle.alphabet_status = status
    gotten = my_wordle.get_string_status()
    expected_string = "\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nAAXO????O????????O????????"
    assert gotten == expected_string


# テストしやすさ: 高い、重要度: 高い
# TODO: プレイヤーが単語を入力したら、入力した単語が正解の文字と一致していたか記号を使って結果を表示する
# TODO: 入力された単語の文字と正解の単語の文字の位置と種類が一致していたら'O'でそのことを伝える
# TODO: 入力された単語の文字が正解の単語の中で使われていたら'A'でそのことを伝える
# TODO: 入力された単語の文字が正解の単語で使われていなかったら'X'でそのことを伝える
# TODO: ゲーム開始時にアルファベットの一覧を表示する
# - [x] アルファベットのリストを返す
# TODO: 入力された単語の文字が正解の単語で使われていなかったらアルファベットの一覧でそのことを伝える
# - [x] アルファベットのリストの下に正解に使われているかわかったらO、使われていないならX、不明なら?となっている文字列を返す
# TODO: 入力された文字を全部大文字に変える

# テストしやすさ: 低い、重要度: 高い
# テストしやすさ: 高い、重要度: 低い
# テストしやすさ: 低い、重要度: 低い

# TODO: 決められた回数だけプレイヤーが単語を入力する
# TODO: 決められた回数の中で入力された単語が正解と一致していたらプレイヤーが勝ち
# TODO: ゲームのたびに正解の単語が変わる
