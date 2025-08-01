# functions/generate_motivating_scenario.py

from google.genai import types


schema_generate_motivating_scenario = types.FunctionDeclaration(
    name="generate_motivating_scenario",
    description="""
    Generate a motivating scenario for ontology development from a domain description.
    The output must follow this structure:

    ---
    # Name
    <A short title that captures the conceptual problem or modeling issue at an abstract level>
    
    # Description
    <A natural language description that illustrates the modeling issue through a concrete example>

    # Examples
    <One or more examples according to the description>
    ---

    Return the entire scenario as a single string.
    In the description, do not refer to anything outside the concrete example.

    """,
    parameters={
        "type": "object",
        "properties": {
            "domain_description": {
                "type": "string",
                "description": "A description of the domain or modeling problem"
            }
        },
        "required": ["domain_description"]
    }
)


def generate_motivating_scenario(domain_description: str) -> str:
    return domain_description
