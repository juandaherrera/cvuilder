from enum import Enum

import reflex as rx


class BaseColor(Enum):
    """
    Base color palette for the app.
    Each color should have a tuple with two values:
    - The first value is the light color.
    - The second value is the dark color.
    """

    def __getattribute__(self, name):
        if name == "value":
            attribute = super().__getattribute__(name)
            light_color = (
                rx.color(*attribute[0]) if isinstance(attribute[0], tuple) else attribute[0]
            )
            dark_color = (
                rx.color(*attribute[1]) if isinstance(attribute[1], tuple) else attribute[1]
            )
            return rx.color_mode_cond(light=light_color, dark=dark_color)
        return super().__getattribute__(name)

    @property
    def color_name(self):
        attribute = super().__getattribute__("value")
        light_color_name = attribute[0][0] if isinstance(attribute[0], tuple) else attribute[0]
        dark_color_name = attribute[1][0] if isinstance(attribute[1], tuple) else attribute[1]
        return rx.color_mode_cond(light=light_color_name, dark=dark_color_name)


class Color(BaseColor):
    """
    Color palette for the app.
    Each color should have a tuple with two values:
    - The first value is the light color.
    - The second value is the dark color.
    """

    PRIMARY = (("indigo", 9), ("indigo", 9))
    SECONDARY = ("#FF9B9B", "#FF9B9B")
    TERTIARY = ("#F1E0C5", "#041523")
    BACKGROUND = (("mauve", 1), ("mauve", 1))
    NAVBAR = (("mauve", 1), ("mauve", 1))
    BORDERS = (
        f"1px solid {rx.color('mauve', 4)}",
        f"1px solid {rx.color('mauve', 4)}",
    )


class TextColor(BaseColor):
    """
    Text color palette for the app.
    Each color should have a tuple with two values:
    - The first value is the light color.
    - The second value is the dark color.
    """

    ACCENT = (("mauve", 11), ("mauve", 11))
    PRIMARY = (("mauve", 12), ("mauve", 12))
