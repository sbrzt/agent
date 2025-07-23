# main.py

import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from config import system_prompt, MODEL_NAME
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file


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

        available_functions = genai.types.Tool(
            function_declarations=[
                schema_get_files_info,
                schema_get_files_content,
                schema_run_python_file
            ]
        )

        response = client.models.generate_content(
            model=MODEL_NAME, 
            contents=messages,
            config=genai.types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )
        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
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
