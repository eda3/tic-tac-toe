from __future__ import annotations

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

    @staticmethod
    def from_notation(notation: str) -> FillAction:
        """ アクション記法(x:c1) -> FillActionオブジェクトの変換"""

        # 記法の入力チェック
        if FillAction.is_valid_notation(notation) is False:
            raise Exception("記法が正しくありません")

        # 一文字目から、o or xを取得
        player_char: str = notation[0]

        # 三文字目から、行番号を取得
        row_num: int = {"a": 0, "b": 1, "c": 2}[notation[2]]

        # 4文字目から列番号を取得
        col_num: int = int(notation[3]) - 1

        # 盤面全体のインデックス番号を取得
        square_index: int = row_num * 3 + col_num

        return FillAction(player_char, square_index)

    def to_notation(self) -> str:
        """FillAction -> アクション記法(x:c1)に変換"""
        row_num = self._square_index // 3
        row_alphabet = ["a", "b", "c"][row_num]
        col_num = self._square_index % 3 + 1

        return f"{self._player_char}:{row_alphabet}{col_num}"
