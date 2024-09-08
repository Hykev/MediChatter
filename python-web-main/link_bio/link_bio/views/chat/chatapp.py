# chatapp.py
import reflex as rx
from link_bio.components.title import title

from link_bio.views.chat import style
from link_bio.views.chat.state import TutorialState

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.vstack(
        rx.input(
            placeholder="Ingresa tu síntoma o consulta",
            value=TutorialState.question,
            on_change=TutorialState.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Enviar",
            on_click=TutorialState.answer,
        ),
    )

def medichat() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center", 
        )
    )
