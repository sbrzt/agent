import os
from google import genai

def create_samod_test_case(test_case_name: str, motivating_scenario: str) -> genai.types.Part:
    base_path = os.path.join("test_cases", test_case_name)
    os.makedirs(base_path, exist_ok=True)

    output_path = os.path.join(base_path, "motivating_scenario.md")
    with open(output_path, "w") as f:
        f.write(motivating_scenario.strip())

    return genai.types.Part(
        function_response=genai.types.FunctionResponse(
            name="create_samod_test_case",
            response={"status": "success", "path": output_path}
        )
    )

schema_create_samod_test_case = genai.types.FunctionDeclaration(
    name="create_samod_test_case",
    description="Create a new SAMOD test case folder and save the motivating scenario",
    parameters={
        "type": "object",
        "properties": {
            "test_case_name": {
                "type": "string",
                "description": "A short name for the test case, used as the folder name"
            },
            "motivating_scenario": {
                "type": "string",
                "description": "The motivating scenario to be saved in the test case folder"
            }
        },
        "required": ["test_case_name", "motivating_scenario"]
    }
)