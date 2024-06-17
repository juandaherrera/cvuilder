from enum import Enum
from typing import Self, Union

import reflex as rx

from .colors import Color, TextColor


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    DEFAULT_MEDIUM = "1.125em"
    DEFAULT_BIG = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    LARGE = "5em"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    DEFAULT_MEDIUM = "5"
    DEFAULT_BIG = "6"
    BIG = "7"
    VERY_BIG = "8"
    LARGE = "9"


GENERAL_PAGE_PADDING_X = ["3em", "8em", "10em", "15em"]


NAVBAR_STYLE = dict(
    position="sticky",
    bg=rx.color(Color.NAVBAR.color_name, 1),
    color=TextColor.PRIMARY.value,
    padding_x=GENERAL_PAGE_PADDING_X,
    border_bottom=Color.BORDERS.value,
    padding_y=Size.DEFAULT.value,
    z_index="999",
    top="0",
    width="100%",
)

FOOTER_STYLE = dict(
    width="100%",
    size=Spacing.DEFAULT.value,
    padding_y=Size.DEFAULT_BIG.value,
    padding_x=GENERAL_PAGE_PADDING_X,
    bg=Color.BACKGROUND.value,
    color=TextColor.ACCENT.value,
    border_top=Color.BORDERS.value,
)
