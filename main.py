# main.py

import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from config import system_prompt, MODEL_NAME
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from functions.create_samod_test_case import schema_create_samod_test_case
from functions.generate_motivating_scenario import schema_generate_motivating_scenario
from functions.generate_informal_competency_questions import schema_generate_informal_competency_questions


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
                schema_get_file_content,
                schema_run_python_file,
                schema_write_file,
                schema_create_samod_test_case,
                schema_generate_motivating_scenario,
                schema_generate_informal_competency_questions
            ]
        )

        loops = 1

        while loops <= 20:
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME, 
                    contents=messages,
                    config=genai.types.GenerateContentConfig(
                        tools=[available_functions],
                        system_instruction=system_prompt
                    )
                )

                if response.candidates:
                    for candidate in response.candidates:
                        messages.append(candidate.content)

                if response.function_calls:
                    for function_call_part in response.function_calls:
                        function_call_result = call_function(function_call_part)
                        if function_call_result.parts[0].function_response.response:
                            if args.verbose:
                                print(f"Has function calls: {bool(response.function_calls)}")
                                print(f"Has text: {bool(response.text)}")
                                if response.function_calls:
                                    for fc in response.function_calls:
                                        print(f" - Calling function: {fc.name}")

                                print(f"-> {function_call_result.parts[0].function_response.response}")
                            tool_message = genai.types.Content(
                                role="tool",
                                parts=[function_call_result.parts[0]]
                            )
                            messages.append(tool_message)
                        else:
                            raise Exception("Function call failed")

                elif response.text:
                    print(f"Final response:\n{response.text}")
                    break

                loops += 1 

            except Exception as e:
                print(f"Error occurred: {e}")
                break

        if args.verbose:
            print(f"User prompt: {args.prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        print("Error: prompt not provided.")
        sys.exit(1)



if __name__ == "__main__":
    main()
