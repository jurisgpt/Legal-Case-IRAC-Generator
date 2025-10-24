import reflex as rx
from app.states.legal_state import LegalState
from app.components.input_screen import input_screen
from app.components.output_screen import output_screen


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.cond(LegalState.show_output, output_screen(), input_screen()),
            class_name="w-full min-h-screen bg-gray-50 flex items-center justify-center p-4 transition-opacity duration-300",
        ),
        class_name="font-['Raleway']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)