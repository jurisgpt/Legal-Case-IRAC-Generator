import reflex as rx
import asyncio
from typing import TypedDict


class IRACSection(TypedDict):
    issue: str
    rule: str
    application: str
    conclusion: str


class LegalState(rx.State):
    case_description: str = ""
    is_loading: bool = False
    show_output: bool = False
    irac_analysis: IRACSection = {
        "issue": "",
        "rule": "",
        "application": "",
        "conclusion": "",
    }

    @rx.event
    def update_irac_section(self, section: str, value: str):
        self.irac_analysis[section] = value

    @rx.var
    def is_button_disabled(self) -> bool:
        return self.is_loading or self.case_description.strip() == ""

    @rx.event(background=True)
    async def generate_irac(self):
        async with self:
            self.is_loading = True
        await asyncio.sleep(2)
        async with self:
            input_len = len(self.case_description)
            if input_len < 50:
                self.irac_analysis = {
                    "issue": "The primary legal issue is whether the provided case description is sufficiently detailed for a meaningful analysis.",
                    "rule": "A legal analysis requires a clear and comprehensive set of facts. Vague or overly brief descriptions prevent the application of relevant legal principles.",
                    "application": "The provided text is very short. It lacks the necessary details about the parties involved, the sequence of events, and the specific harm or dispute alleged. Therefore, a proper legal rule cannot be applied.",
                    "conclusion": "The analysis cannot be completed due to insufficient information. Please provide a more detailed case description.",
                }
            else:
                self.irac_analysis = {
                    "issue": "The central issue appears to be a potential breach of contract regarding the delivery of specified goods.",
                    "rule": "A breach of contract occurs when one party fails to fulfill its obligations under the contract without a legal excuse. The non-breaching party may be entitled to damages.",
                    "application": f"The case description, which is approximately {input_len} characters long, suggests that Party A failed to deliver goods to Party B by the agreed-upon date. This failure to perform as specified in the agreement constitutes a breach.",
                    "conclusion": "Based on the preliminary facts, Party B likely has a valid claim for breach of contract against Party A.",
                }
            self.is_loading = False
            self.show_output = True

    @rx.event
    def analyze_another_case(self):
        self.show_output = False
        self.case_description = ""
        self.irac_analysis = {
            "issue": "",
            "rule": "",
            "application": "",
            "conclusion": "",
        }