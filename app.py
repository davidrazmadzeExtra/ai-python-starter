from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
previous_response_id = None

print("AI Technical Tutor")
print("Type 'quit' to exit. \n")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
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
		input=question,
        previous_response_id=previous_response_id
	)
    print(f"\nAI: {response.output_text}\n")
    
    previous_response_id = response.id

print("\nAI:")
print(response.output_text)
