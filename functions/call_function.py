# functions/call_function.py

from google import genai
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

from functions.create_samod_test_case import create_samod_test_case
from functions.generate_motivating_scenario import generate_motivating_scenario
from functions.generate_informal_competency_questions import generate_informal_competency_questions


function_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
    "create_samod_test_case": create_samod_test_case,
    "generate_motivating_scenario": generate_motivating_scenario,
    "generate_informal_competency_questions": generate_informal_competency_questions
}


def call_function(function_call_part, verbose=False):
    if function_call_part.name not in function_map:
        return genai.types.Content(
            role="tool",
            parts=[
                genai.types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    actual_function = function_map[function_call_part.name]
    result = actual_function(**function_call_part.args)

    return genai.types.Content(
        role="tool",
        parts=[
            genai.types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    ) 

