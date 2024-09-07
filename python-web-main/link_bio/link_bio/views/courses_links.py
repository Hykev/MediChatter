import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size, Color, Spacing
from link_bio.routes import Route

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Estadísticas"),
        link_button(
                "Regresar",
                "¡Continúa hablando con MediChatter!",
                "/icons/return.png",
                Route.INDEX.value,
                False,
                Color.SECONDARY.value
            ),






            rx.link(
                rx.hstack(
                    rx.text(
                        "Expectativa de vida al nacer a nivel global",
                        font_size=Size.DEFAULT.value,
                        margin_top=Size.ZERO.value
                    ),
                ),
                href="https://ourworldindata.org/grapher/life-expectancy",
                is_external=True
            ),

            rx.recharts.area_chart(
                rx.recharts.area(
                    data_key="edad",
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                data=data_life,
                width="100%",
                height=200,
            ),







            rx.link(
                rx.hstack(
                    rx.text(
                        "Muertes por diabetes a nivel mundial en los últimos 50 años.",
                        font_size=Size.DEFAULT.value,
                        margin_top=Size.ZERO.value
                    ),
                ),
                href="https://ourworldindata.org/grapher/deaths-from-diabetes-by-type",
                is_external=True
            ),

             rx.recharts.area_chart(
                rx.recharts.area(
                    data_key="muertes",
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                data=data_diabetes,
                width="100%",
                height=200,
            ),







            rx.link(
                rx.hstack(
                    rx.text(
                        "Muertes por COVID-19 estimadas de forma acumulativa a nivel mundial (en millones).",
                        font_size=Size.DEFAULT.value,
                        margin_top=Size.ZERO.value
                    ),
                ),
                href="https://ourworldindata.org/grapher/excess-deaths-cumulative-economist-single-entity",
                is_external=True
            ),

             rx.recharts.area_chart(
                rx.recharts.area(
                    data_key="muertes",
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                data=data_covid,
                width="100%",
                height=200,
            ),





            rx.link(
                rx.hstack(
                    rx.text(
                        "Muertes por cancer (en cientos de miles)",
                        font_size=Size.DEFAULT.value,
                        margin_top=Size.ZERO.value
                    ),
                ),
                href="https://ourworldindata.org/grapher/cancer-death-rates?tab=chart",
                is_external=True
            ),

             rx.recharts.area_chart(
                rx.recharts.area(
                    data_key="muertes",
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                data=data_cancer,
                width="100%",
                height=200,
            ),

        width="100%",
        spacing=Spacing.DEFAULT.value,
    )
        
data_life = [
    {"name": "1910", "edad": 34.1},
    {"name": "1940", "edad": 39.7},
    {"name": "1970", "edad": 56.1},
    {"name": "2000", "edad": 66.5},
    {"name": "2020", "edad": 71.0},
]

data_diabetes = [
    {"name": "1980", "muertes": 515678},
    {"name": "1990", "muertes": 672022},
    {"name": "2000", "muertes": 897303},
    {"name": "2010", "muertes": 1170000},
    {"name": "2020", "muertes": 1660000},
]

data_covid = [
    {"name": "2020", "muertes": 0},
    {"name": "2021", "muertes": 5.94},
    {"name": "2022", "muertes": 16.02},
    {"name": "2023", "muertes": 22.94},
    {"name": "2024", "muertes": 26.1},
]

data_cancer = [
    {"name": "1980", "muertes": 153.5},
    {"name": "1990", "muertes": 148.2},
    {"name": "2000", "muertes": 140.8},
    {"name": "2010", "muertes": 127.4},
    {"name": "2020", "muertes": 116.5},
]