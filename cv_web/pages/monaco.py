from typing import Any, Literal

from reflex.components.component import Component
from reflex.vars import Var

"""Editor built-in themes"""
Theme = Literal["light", "vs-dark"]


class MonacoEditor(Component):
    """React Monaco Editor Component"""

    library = "@monaco-editor/react"
    tag = "Editor"
    alias = "MonacoEditor"
    lib_dependencies: list[str] = ["@monaco-editor/react"]
    #
    # Props
    #
    """Default programming language"""
    defaultLanguage: Var[str] = "sql"
    """Editor theme"""
    theme: Var[Theme]

    #
    # Event triggers
    #
    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_change": lambda e0, e1: [e0, e1],
            "on_validate": lambda e0: [e0],
        }


monaco_editor = MonacoEditor.create
