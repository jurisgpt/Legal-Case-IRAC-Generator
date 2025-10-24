import reflex as rx
from app.states.legal_state import LegalState


def _loading_spinner() -> rx.Component:
    return rx.el.div(
        class_name="animate-spin rounded-full h-5 w-5 border-b-2 border-white"
    )


def input_screen() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag="scale", class_name="w-12 h-12 mx-auto text-emerald-600"),
            rx.el.h1(
                "Legal Case IRAC Analysis",
                class_name="mt-4 text-center text-3xl font-bold tracking-tight text-gray-900",
            ),
            rx.el.p(
                "Describe your legal situation in plain English. Our AI will generate a structured analysis using the Issue, Rule, Application, Conclusion (IRAC) framework.",
                class_name="mt-2 text-center text-sm text-gray-600 max-w-lg mx-auto",
            ),
        ),
        rx.el.div(
            rx.el.textarea(
                name="case_description",
                placeholder="e.g., 'I signed a contract to have my roof repaired by May 1st, but the contractor never showed up and now there's water damage...'",
                on_change=LegalState.set_case_description,
                class_name="w-full h-48 p-4 rounded-lg border border-gray-300 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-shadow duration-150 resize-none text-base font-medium",
            ),
            class_name="mt-8",
        ),
        rx.el.div(
            rx.el.button(
                rx.cond(
                    LegalState.is_loading,
                    _loading_spinner(),
                    rx.el.span("Generate IRAC Analysis"),
                ),
                on_click=LegalState.generate_irac,
                disabled=LegalState.is_button_disabled,
                class_name="w-full flex justify-center items-center px-6 py-3 rounded-lg text-white font-semibold shadow-md bg-gradient-to-r from-emerald-500 to-emerald-700 hover:from-emerald-600 hover:to-emerald-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 transition-all duration-200 ease-in-out transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none",
            ),
            class_name="mt-6",
        ),
        class_name="w-full max-w-2xl bg-white p-8 rounded-xl shadow-lg border border-gray-200",
    )