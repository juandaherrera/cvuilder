import reflex as rx

from cv_web.styles.colors import Color, TextColor
from cv_web.styles.styles import NAVBAR_STYLE, Size, Spacing


def link_item(name: str, url: str):
    return rx.link(
        rx.center(
            rx.text(
                name,
                color=TextColor.ACCENT.value,
                font="Instrument Sans",
                style={"font-size": "16px"},
                weight="medium",
            ),
            height="100%",
        ),
        href=url,
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size=Spacing.DEFAULT.value, weight="medium", color=TextColor.PRIMARY.value),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "CVuilder 🚀",
                        size=Spacing.VERY_BIG.value,
                        weight="bold",
                        color=Color.PRIMARY.value,
                        # margin_right=Size.DEFAULT_MEDIUM.value,
                    ),
                    rx.divider(
                        orientation="vertical",
                        height=Size.DEFAULT_BIG.value,
                        margin_x=Size.DEFAULT_MEDIUM.value,
                    ),
                    rx.hstack(
                        link_item("Home", "/#"),
                        link_item("About", "/#"),
                        link_item("Pricing", "/#"),
                        link_item("Contact", "/#"),
                        spacing=Spacing.DEFAULT_BIG.value,
                    ),
                    align_items="center",
                ),
                rx.color_mode.button(justify="end"),
                color=TextColor.ACCENT.value,
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "CVuilder 🚀",
                        size=Spacing.VERY_BIG.value,
                        weight="bold",
                        color=Color.PRIMARY.value,
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.item("Earnings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        style=NAVBAR_STYLE,
        # bg=rx.color("accent", 3),
        # padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        # width="100%",
    )
