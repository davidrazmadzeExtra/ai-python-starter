from openai import OpenAI

from config import MODEL
from models import LearningResponse


client = OpenAI()


def ask_ai(question: str) -> tuple[LearningResponse, object]:
    response = client.responses.parse(
        model=MODEL,
        instructions="""
        You are a technical tutor for software engineers.

        Explain concepts clearly and concisely.
        Assume the user understands programming.
        Include examples when useful.
        """,
        input=question,
        text_format=LearningResponse,
    )

    return response.output_parsed, response.usage