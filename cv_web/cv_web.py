"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from cv_web.pages import index


class State(rx.State):
    """The app state."""

    ...


app = rx.App()
