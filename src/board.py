from __future__ import annotations

import re
from re import Pattern


class Board:
    squares_string: str

    def __init__(self, squares_string: str) -> None:
        if len(squares_string) != 9:
            raise Exception("Boardクラスの初期化は9文字でなければなりません。")
        self.squares_string = squares_string

    @staticmethod
    def is_valid_notation(notation: str) -> bool:
        """記法の妥当性チェック"""
        match_str: str = r"^\[.{3},.{3},.{3}\]$"
        pattern: Pattern = re.compile(match_str)

        return True if pattern.match(notation) else False

    @staticmethod
    def from_notation(notation: str) -> Board:
        """ 記法 -> Boardオブジェクトの変換"""
        if Board.is_valid_notation(notation) is False:
            raise Exception("記法が正しくありません")

        # 数値部分だけを抜き取る
        squares_string: str = notation[1:4] + notation[5:8] + notation[9:12]

        return Board(squares_string)

    def to_notation(self) -> str:
        """ Boardオブジェクト -> 記法の変換"""
        return (
            "["
            + self.squares_string[0:3]
            + ","
            + self.squares_string[3:6]
            + ","
            + self.squares_string[6:9]
            + "]"
        )
