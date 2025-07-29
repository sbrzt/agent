# agent

## Description
An agentic CLI tool that:
- Accepts a coding task
- Chooses from a set of predefined functions to work on the task, for example:
    - Scan the files in a directory
    - Read a file's contents
    - Overwrite a file's contents
    - Execute the Python interpreter on a file
- Repeats step 2 until the task is complete or fails

## To do

### Extend Function Schemas for Ontology Tasks
Add new tool schemas (functions the LLM can call), such as:
- `schema_generate_motivating_scenario`
    - Input: domain description
    - Output: motivating scenario text with examples
- `schema_generate_glossary`
    - Input: motivating scenario
    - Output: glossary of terms (JSON or Markdown)
- `schema_generate_competency_questions`
    - Input: motivating scenario
    - Output: structured list of competency questions
- `schema_generate_modelet`
    - Input: glossary + competency questions
    - Output: OWL/Turtle RDF using rdflib or templates
- `schema_generate_abox`
    - Input: modelet + examples
    - Output: ABox (data instance triples)
- `schema_generate_sparql_queries`
    - Input: competency questions + TBox
    - Output: SPARQL query list (as text or .rq files)
- `schema_run_model_test`, `schema_run_data_test`, `schema_run_query_test`
    - Use rdflib, owlrl, or call to HermiT, Pellet, or even ROBOT