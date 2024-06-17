from datetime import datetime

import reflex as rx

import cv_web.constants as const
from cv_web import __VERSION__
from cv_web.styles.colors import Color, TextColor
from cv_web.styles.styles import FOOTER_STYLE, Size, Spacing


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                f"© {datetime.today().year} by ",
                rx.link("juandaherrera", href=const.GUTHUB_URL, is_external=True),
                ". All rights reserved.",
            ),
            rx.text(f"v{__VERSION__}"),
            rx.text(
                "Made with ❤️ from Palmira, Colombia 🇨🇴.",
            ),
            justify="between",
            align_items="center",
            style=FOOTER_STYLE,
        ),
        width="100%",
    )
