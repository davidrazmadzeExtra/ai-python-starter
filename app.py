from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

question = input("Ask AI anything: ")

response = client.responses.create(
	model="gpt-5.4-mini",
	input=question
)

print("\nAI:")
print(response.output_text)
