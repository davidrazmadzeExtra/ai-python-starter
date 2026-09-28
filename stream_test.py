from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

question = input("What would you like to learn? ")

stream = client.responses.create(
    model="gpt-5.4-mini",
    instructions="""
    You are a technical tutor for software engineers.
    Explain concepts clearly and concisely.
    """,
    input=question,
    stream=True
)

print("\nAI: ", end="", flush=True)

for event in stream:
    if event.type == "response.output_text.delta":
        # A delta is essentially the new piece of text that has arrived since the previous event.

        # prevents Python from inserting a newline after every chunk.
        print(event.delta, end="", flush=True)

print()