import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size, Spacing
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor


def medichat() -> rx.Component:
    return rx.vstack(
        
        title("CHAT"),
    )