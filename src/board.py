import re
from re import Pattern


class Board:
    def __init__(self, squares_string):
        if len(squares_string) != 9:
            raise Exception("Boardクラスの初期化は9文字でなければなりません。")
        self._squares_string = squares_string

    @staticmethod
    def is_valid_notation(notation: str) -> bool:
        """記法の妥当性チェック"""
        match_str: str = r"^\[.{3},.{3},.{3}\]$"
        pattern: Pattern = re.compile(match_str)

        return True if pattern.match(notation) else False
