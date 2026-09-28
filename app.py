from dotenv import load_dotenv
from openai import OpenAI, APIError

from models import LearningResponse

load_dotenv()

client = OpenAI()

question = input("What would you like to learn? ")

try:
    response = client.responses.parse(
        model="gpt-does-not-exist-model",
        instructions="""
        You are a technical tutor for software engineers.

        Explain concepts clearly and concisely.
        Assume the user understands programming.
        """,
        input=question,
        text_format=LearningResponse,
    )

    result = response.output_parsed

    print("\nANSWER")
    print(result.answer)

    print(f"\nDIFFICULTY: {result.difficulty}/10")

    print("\nKEY POINTS")
    for point in result.key_points:
        print(f"- {point}")

    print("\nTOPICS")
    for topic in result.topics:
        print(f"- {topic}")

    print("\nFOLLOW-UP")
    print(result.follow_up_question)

    print("\nUSAGE")
    print(f"Input tokens: {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")
    print(f"Total tokens: {response.usage.total_tokens}")

except APIError as error:
    print(f"\nOpenAI API error: {error}")

except Exception as error:
    print(f"\nUnexpected error: {error}")