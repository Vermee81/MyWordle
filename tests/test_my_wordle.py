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


def test_入力した1文字が位置して1文字が存在して他はハズレ(my_wordle):
    input_word = "BLIND"
    ans_word = "PRIDE"
    expected = "\nBLIND\nXXOXA"
    gotten = my_wordle.get_result(input_word, ans_word)
    assert gotten == expected


def test_入力した文字が全部ハズレ(my_wordle):
    input_word = "BLIND"
    ans_word = "STAMP"
    expected = "\nBLIND\nXXXXX"
    gotten = my_wordle.get_result(input_word, ans_word)
    assert gotten == expected


# 同じ文字が連続して使われていた時に、MATCHEDとAVAILABLEを正しく返す
def test_同じ文字が連続して使われていた時にMATCHEDとAVAILABLEを正しく返す(my_wordle):
    input_word = "IIIII"
    ans_word = "SPLIT"
    expected = "\nIIIII\nAAAOA"
    gotten = my_wordle.get_result(input_word, ans_word)
    assert gotten == expected


def test_入力した文字が全部正解していたらTrue(my_wordle):
    my_wordle.input_status = [
        ["A", STATUS.MATCHED],
        ["B", STATUS.MATCHED],
        ["C", STATUS.MATCHED],
    ]
    gotten = my_wordle.is_all_matched()
    assert gotten == True


def test_入力した文字が1文字でも不正解ならFalse(my_wordle):
    my_wordle.input_status = [
        ["Z", STATUS.MATCHED],
        ["X", STATUS.AVAILABLE],
        ["Y", STATUS.UNKNOWN],
    ]
    gotten = my_wordle.is_all_matched()
    assert gotten == False


# テストしやすさ: 高い、重要度: 高い
# TODO: ゲーム開始時にアルファベットの一覧を表示する

# テストしやすさ: 低い、重要度: 高い
# テストしやすさ: 高い、重要度: 低い
# テストしやすさ: 低い、重要度: 低い
