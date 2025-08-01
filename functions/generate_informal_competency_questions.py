# functions/generate_informal_competency_questions.py

from google.genai import types


schema_generate_informal_competency_questions = types.FunctionDeclaration(
    name="generate_informal_competency_questions",
    description=("""
        Generate a set of informal competency questions (ICQs) based on a given motivating scenario.
        Each ICQ must be structured with the following fields:
        - identifier: a unique numeric identifier (integer or string)
        - question: a natural language question representing an informal domain requirement
        - outcome: the expected type or format of the answer
        - examples: some exemplar answers, based on the motivating scenario
        - depends_on: a list of identifiers of higher-level ICQs this question depends on (may be empty)
        "Return the list of ICQs as a JSON array of objects with those fields.
        """
    ),
    parameters={
        "type": "object",
        "properties": {
            "motivating_scenario": {
                "type": "string",
                "description": "The motivating scenario text from which to derive the competency questions."
            }
        },
        "required": ["motivating_scenario"]
    }
)


def generate_informal_competency_questions(motivating_scenario: str) -> str:
    return motivating_scenario

