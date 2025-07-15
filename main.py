import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():

    if len(sys.argv) > 1:
        if type(sys.argv[1]) == str:
            user_prompt = sys.argv[1]
            messages = [
                genai.types.Content(
                    role="user",
                    parts=[
                        genai.types.Part(
                            text=user_prompt
                        ),
                    ]
                )
            ]
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", 
                contents=messages,
            )
    else:
        print("Error: prompt not provided.")
        sys.exit(1)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
