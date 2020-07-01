import sys
import os
import pytest
from board import Board


def test_is_valid_notation():
    board = Board("123456789")
    assert board.is_valid_notation("[123,456,789]") is True
    assert board.is_valid_notation("aaa") is False


def test_from_notation():
    board = Board("123456789")

    # 引数が正しくない場合、例外が発生する
    with pytest.raises(Exception):
        board.from_notation("aaa")

    # 引数が正しい場合、数値部分を含むBoardインスタンスが返却される
    new_board = board.from_notation("[123,456,789]")
    assert new_board.squares_string == "123456789"
