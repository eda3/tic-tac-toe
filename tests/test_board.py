import sys
import os
import pytest
from board import Board


def test_is_valid_notation():
    board = Board("123456789")
    assert board.is_valid_notation("[123,456,789]") is True
    assert board.is_valid_notation("aaa") is False
