import reflex as rx

from cv_web.components.shared import footer, navbar
from cv_web.styles.colors import Color, TextColor
from cv_web.styles.styles import GENERAL_PAGE_PADDING_X, Size, Spacing

from .monaco import monaco_editor


class IndexState(rx.State):
    query: str = "Select * from table_name;"

    def set_query(self, value: str):
        self.query = value

    def execute_query(self):
        # Implementa la lógica para ejecutar la consulta SQL aquí
        pass


@rx.page(
    route="/",
    title="CVuilder 🚀",
    # description=const.INDEX_DESCRIPTION,
    # image=const.INDEX_PREVIEW,
    # meta=const.INDEX_META,
)
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            index_hook(),
            min_height="80vh",
            width="100%",
            padding_x=GENERAL_PAGE_PADDING_X,
        ),
        footer(),
        spacing="5",
        min_height="100vh",
        width="100%",
        bg=Color.BACKGROUND.value,
    )


def index_hook() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                rx.text("Build your CV in less than 15 minutes"),
                size=Spacing.VERY_BIG.value,
                color=Color.PRIMARY.value,
                margin_bottom=Size.SMALL.value,
                text_align="center",
            ),
            rx.text(
                "Forget about design and focus on writing your CV. Our tool ensures your "
                "resume is optimized for Applicant Tracking Systems (ATS), helping you stand out to employers.",
                size=Spacing.SMALL.value,
                color=TextColor.PRIMARY.value,
                width="90%",
            ),
            align_items="left",
            width="100%",
        ),
        rx.vstack(
            rx.vstack(
                monaco_editor(
                    value=IndexState.query, theme=rx.color_mode_cond(light="light", dark="vs-dark")
                ),
                rx.button("Execute", on_click=IndexState.execute_query),
                width="100%",
                height="500px",
            ),
            align_items="left",
            width="100%",
        ),
        padding_y=Size.BIG.value,
        width="100%",
    )
