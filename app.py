from dotenv import load_dotenv
from openai import OpenAI

from models import LearningResponse

load_dotenv()

client = OpenAI()

question = input("What would you like to learn? ")

response = client.responses.parse(
    model="gpt-5.4-mini",
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

print("\nKEY POINTS")
for point in result.key_points:
    print(f"- {point}")

print("\nTOPICS")
for topic in result.topics:
    print(f"- {topic}")

print("\nFOLLOW-UP")
print(result.follow_up_question)