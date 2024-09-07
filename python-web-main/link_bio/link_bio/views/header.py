import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import Color, TextColor
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.avatar(
                    name="",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/avatar.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="-px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.hstack (

                    rx.heading(
                        "Medi Chatter",
                        size=Spacing.BIG.value
                    ),
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                ),
                    rx.text(
                        "Asistente médico virtual",
                        margin_top=Size.ZERO.value,
                        color=Color.PRIMARY.value
                    ),
                
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    rx.spacer(),
                    info_text(
                        "*", "El chatbot puede llegar a dar datos erróneos."
                    ),
                    rx.spacer(),
                    info_text(
                        "*", "No se automedique; obtenga un diagnóstico adecuado."
                    ),
                    width="100%"
                ),
                rx.text(
                    f"""
                    Soy Medichatter, tu asistente de salud virtual. Aquí para ayudarte con tus dudas sobre medicina.
                    Recuerda que aunque puedo proporcionarte información útil, siempre es recomendable consultar a tu
                    médico para un diagnóstico y tratamiento adecuados.
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
    )

