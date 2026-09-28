from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

question = input("What would you like to learn? ")

response = client.responses.create(
	model="gpt-5.4-mini",
    instructions="""
	You are a technical tutor for software engineers.
    
    When answering:
    - Be concise.
    - Explain concepts in plain English.
    - Assume the user understands programming.
    - Include a simple example when useful.
	""",
	input=question
)

print("\nAI:")
print(response.output_text)
