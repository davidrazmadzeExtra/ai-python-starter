from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

question = input("What would you like to learn? ")

response = client.responses.create(
	model="gpt-5.4-mini",
    instructions="""
	You are teaching someone who has never programmed before.
    Avoid technical jargon.
	""",
	input=question
)

print("\nAI:")
print(response.output_text)
