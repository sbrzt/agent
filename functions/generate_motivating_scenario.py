from google.genai import types

schema_generate_motivating_scenario = types.FunctionDeclaration(
    name="generate_motivating_scenario",
    description="Generate a motivating scenario for ontology development from a domain description",
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
    prompt = f"""
You are helping a knowledge engineer using the SAMOD ontology engineering methodology. 
Generate a motivating scenario for the domain modeling area: "{domain_description}".

Follow this structure exactly:

---
**Name**  
A short title that captures the conceptual problem or modeling issue.

**Description**  
A natural language description that presents the problem to address;

**Examples**  
One or more examples according to the description.

---

Do NOT explain why ontologies are useful. Focus on the modeling issue. Use realistic names and concepts. Be concise and semantically precise.
    """.strip()

    return prompt
