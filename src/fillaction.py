import re
from re import Match, Pattern
from typing import Optional

from board import Board
from gamestate import GameState


class FillAction:
    _player_char: str
    _square_index: int

    def __init__(self, player_char: str, square_index: int) -> None:
        if len(player_char) != 1:
            raise Exception("プレイヤーの文字は一文字でなければなりません")
        elif square_index < 0 or 8 < square_index:
            raise Exception("指定番号は0から8の間でなければなりません")

        self._player_char = player_char
        self._square_index = square_index

    @staticmethod
    def is_valid_notation(notation: str) -> bool:
        """アクション入力内容が正しいかチェック"""
        # 例： x:c2
        match_str: str = r"^.:[a-c][1-3]$"
        pattern: Pattern = re.compile(match_str)
        is_match: Optional[Match] = pattern.match(notation)

        return True if is_match else False
