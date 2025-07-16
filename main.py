import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():

    parser = argparse.ArgumentParser(
        description="Generate a response using Gemini"
        )
    parser.add_argument(
        "prompt", 
        help="Prompt to send to Gemini"
        )
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable verbose output"
        )
    args = parser.parse_args()

    if args.prompt:
        messages = [
            genai.types.Content(
                role="user",
                parts=[
                    genai.types.Part(
                        text=args.prompt
                    ),
                ]
            )
        ]

        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages,
        )

        print(response.text)

        if args.verbose:
            print(f"User prompt: {args.prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}") 
        
    else:
        print("Error: prompt not provided.")
        sys.exit(1)

if __name__ == "__main__":
    main()
