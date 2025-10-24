import reflex as rx
from app.states.legal_state import LegalState


def irac_card(title: str, section_key: str, content: rx.Var[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-semibold text-gray-800 mb-2"),
        rx.el.textarea(
            default_value=content,
            on_change=lambda val: LegalState.update_irac_section(section_key, val),
            class_name="w-full h-48 p-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-shadow duration-150 resize-y text-base font-medium text-gray-600 leading-relaxed bg-white",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm transition-all duration-200 hover:shadow-md hover:border-gray-300",
    )


def _skeleton_loader() -> rx.Component:
    return rx.el.div(
        rx.el.div(class_name="h-4 bg-gray-200 rounded w-1/4 mb-4"),
        rx.el.div(class_name="h-3 bg-gray-200 rounded w-full mb-2"),
        rx.el.div(class_name="h-3 bg-gray-200 rounded w-5/6"),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm animate-pulse",
    )


def output_screen() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "IRAC Analysis", class_name="text-3xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                "Here is the structured breakdown of your legal case.",
                class_name="text-sm text-gray-600",
            ),
            class_name="text-center mb-8",
        ),
        rx.cond(
            LegalState.is_loading,
            rx.el.div(
                _skeleton_loader(),
                _skeleton_loader(),
                _skeleton_loader(),
                _skeleton_loader(),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            rx.el.div(
                irac_card("Issue", "issue", LegalState.irac_analysis["issue"]),
                irac_card("Rule", "rule", LegalState.irac_analysis["rule"]),
                irac_card(
                    "Application",
                    "application",
                    LegalState.irac_analysis["application"],
                ),
                irac_card(
                    "Conclusion", "conclusion", LegalState.irac_analysis["conclusion"]
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        ),
        rx.el.div(
            rx.el.button(
                "Analyze Another Case",
                on_click=LegalState.analyze_another_case,
                class_name="px-6 py-3 rounded-lg text-gray-700 bg-white border border-gray-300 font-semibold shadow-sm hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 transition-all duration-200 ease-in-out transform hover:scale-[1.02]",
            ),
            class_name="mt-8 flex justify-center",
        ),
        class_name="w-full max-w-4xl",
    )