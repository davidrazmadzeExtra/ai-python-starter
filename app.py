from openai import APIError

from llm import ask_ai


def main():
    question = input("What would you like to learn? ")

    try:
        result, usage = ask_ai(question)

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
        print(f"Input tokens: {usage.input_tokens}")
        print(f"Output tokens: {usage.output_tokens}")
        print(f"Total tokens: {usage.total_tokens}")

    except APIError as error:
        print(f"\nOpenAI API error: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()